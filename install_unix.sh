#bush install.sh
python3 -m venv env

source env/bin/activate

python3 -m pip install -U pip

pip install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py collectstatic

python3 manage.py createsuperuser

deactivate