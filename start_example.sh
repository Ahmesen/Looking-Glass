export FLASK_HOST=
export FLASK_APP=app.py
export FLASK_ENV=production
export MAIN_PAGE=
# export TEMPLATES_AUTO_RELOAD = true
/usr/bin/gunicorn --bind 127.0.0.1:5555 app:app
