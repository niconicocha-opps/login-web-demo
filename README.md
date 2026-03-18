# login-web-demo

A tiny local Python Flask web app with username/password authentication.

## Requirements

- Python 3.7+
- Flask

Install Flask:
```bash
pip install flask
```

## Setup

1. Copy `.env.example` to `.env` and customize credentials (optional):
   ```bash
   cp .env.example .env
   ```

2. Run the app:
   ```bash
   python app.py
   ```

3. Open http://127.0.0.1:5000 in your browser

## Default Credentials

If no environment variables are set:
- **Username:** admin
- **Password:** demo123

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `LOGIN_USERNAME` | Login username | admin |
| `LOGIN_PASSWORD` | Login password | demo123 |
| `SECRET_KEY` | Flask secret key | dev-secret-key-change-in-production |

## Usage

- Login with configured credentials
- On success, you'll see a welcome page
- Click "Logout" to end the session

## Notes

- For local development only (runs on 127.0.0.1)
- Not intended for production use (no HTTPS, basic auth)
