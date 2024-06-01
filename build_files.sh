pip install -r requirements.txt

python manage.py collectstatic --no-input

chmod +x delete_specific_from_multiselectfield.py

./delete_specific_from_multiselectfield.py

# python manage.py makemigrations

# python manage.py migrate

# python -m gunicorn flairest_project.asgi:application -k uvicorn.workers.UvicornWorker - off
# python manage.py runserver - on