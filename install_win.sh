#bush install.sh
python -m venv env

env/Scripts/activate

python -m pip install -U pip

pip install -r requirements.txt

python manage.py makemigrations butler

python manage.py migrate

python manage.py collectstatic

python manage.py createsuperuser

deactivate