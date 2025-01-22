# Django + Aiogram

## 1. GO

- Go project path

```sh
cd <folder name>
```

## 2. Create virtualenv and activate

```sh
python3 -m virtualenv venv
source venv/bin/activate
```

## 3. Install required packages

```sh
pip install -r requirements.txt
```

## 4. Create ```.env``` file using env template file and fill it

```sh
cp .env.template .env
```

## 5. Run django project

- Migrations

```sh
python manage.py migrate
```

- superuser
```sh
python manage.py createsuperuser
```

- Run server

```sh
python manage.py runserver
```

## 6. Run aiogram project

```sh
python manage.py runbot
```

> Django admin will be on http://<your server ip>:8000/admin
> creds are what you did in createsuperuser

