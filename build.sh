set -o errexit  # Exit on error

pip install -r requirements.txt

python manage.py migrate
if [[ -n "$CREATE_SUPERUSER" ]]; then
    python manage.py createsuperuser --noinput --email "$DJANGO_SUPERUSER_EMAIL"
fi
