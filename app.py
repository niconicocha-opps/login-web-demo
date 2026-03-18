import os
from flask import Flask, request, render_template_string, redirect, url_for, session, flash
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

# Load credentials from environment variables with demo defaults
USERNAME = os.environ.get('LOGIN_USERNAME', 'admin')
PASSWORD = os.environ.get('LOGIN_PASSWORD', 'demo123')
HOST = os.environ.get('HOST', '127.0.0.1')
PORT = int(os.environ.get('PORT', '5000'))
DEBUG = os.environ.get('FLASK_DEBUG', 'true').lower() in {'1', 'true', 'yes', 'on'}

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f5f5f5; }
        .login-box { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 300px; }
        h2 { margin-top: 0; color: #333; text-align: center; }
        input { width: 100%; padding: 10px; margin: 10px 0; box-sizing: border-box; border: 1px solid #ddd; border-radius: 4px; }
        button { width: 100%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        button:hover { background: #0056b3; }
        .error { color: red; text-align: center; margin: 10px 0; }
        .hint { color: #666; text-align: center; font-size: 13px; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Login</h2>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <div class="error">{{ messages[0] }}</div>
            {% endif %}
        {% endwith %}
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required autofocus>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <div class="hint">Configure credentials via environment variables or a local .env file.</div>
    </div>
</body>
</html>
'''

PROTECTED_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f5f5f5; }
        .box { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); text-align: center; }
        h2 { color: #28a745; }
        p { color: #666; }
        a { color: #007bff; text-decoration: none; }
    </style>
</head>
<body>
    <div class="box">
        <h2>✓ Login Successful!</h2>
        <p>Welcome, <strong>{{ username }}</strong>!</p>
        <p><a href="/logout">Logout</a></p>
    </div>
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('protected'))

    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        if username == USERNAME and password == PASSWORD:
            session.clear()
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('protected'))

        flash('Invalid username or password')

    return render_template_string(HTML_TEMPLATE)


@app.route('/protected')
def protected():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template_string(PROTECTED_TEMPLATE, username=session.get('username'))


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('login'))


if __name__ == '__main__':
    print('Starting login-web-demo')
    print(f'Listening on http://{HOST}:{PORT}')
    print(f'Default/demo credentials: username={USERNAME}, password={PASSWORD}')
    print('Override with LOGIN_USERNAME, LOGIN_PASSWORD, SECRET_KEY, HOST, PORT, FLASK_DEBUG')
    app.run(host=HOST, port=PORT, debug=DEBUG)
