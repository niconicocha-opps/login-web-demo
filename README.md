# login-web-demo

A tiny local Python Flask web app with username/password authentication.

## Features

- Local login page
- Username/password authentication
- Protected page after successful login
- Logout flow
- Configuration via environment variables or a local `.env` file

## Requirements

- Python 3.8+

## Quick start

```bash
cd /home/robin/.openclaw/workspace/login-web-demo
python3 -m pip install -r requirements.txt
cp .env.example .env
python3 app.py
```

Then open <http://127.0.0.1:5000> in your browser.

## Default demo credentials

If you do not set custom credentials, the app uses:

- **Username:** `admin`
- **Password:** `demo123`

## Configuration

Copy `.env.example` to `.env` and update values as needed:

```bash
cp .env.example .env
```

Supported variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `LOGIN_USERNAME` | Login username | `admin` |
| `LOGIN_PASSWORD` | Login password | `demo123` |
| `SECRET_KEY` | Flask session secret | `dev-secret-key-change-in-production` |
| `HOST` | Bind host | `127.0.0.1` |
| `PORT` | Bind port | `5000` |
| `FLASK_DEBUG` | Debug mode | `true` |

## Notes

- Designed for local development only
- No HTTPS
- No database-backed users
- Not suitable for production authentication

## Project files

- `app.py` — Flask app
- `.env.example` — sample configuration
- `requirements.txt` — Python dependencies
- `.gitignore` — ignores `.env`, `.venv`, and Python cache files
