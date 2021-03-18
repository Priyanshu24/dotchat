# Django Starter Boilerplate

![python](https://img.shields.io/pypi/pyversions/Django?style=for-the-badge)
![django](https://img.shields.io/pypi/v/django?label=Django&logo=Django&style=for-the-badge)
![forks](https://img.shields.io/github/forks/Priyanshu24/django-starter-boilerplate?style=for-the-badge)
![issues](https://img.shields.io/github/issues/Priyanshu24/django-starter-boilerplate?style=for-the-badge)
![license](https://img.shields.io/github/license/Priyanshu24/django-starter-boilerplate?style=for-the-badge)

## What is this ?

This is a simple boilerplate to start your new django project on the go without putting too much time into setting up custom user models( very important ).

## Why should you consider using this ?

Everytime we start some new django project we are compelled to setup custom user authentication which may eat up at anywhere between 20-40 minutes depending on our know-how of django. Also, it is highly advisable to use custom user models whenever we start a new django project. While, it is okay to use the default user model when we are building some small project which we do not intend to scale up, it is a horrendous mistake not to setup custom user model if you intend to scale your project up because the default user model CAN and WILL hamper you from implementing any user related changes which is obviously not the ideal situation.

## Who should use it ?

Developers who have some decent understanding of django can use it. Beginners can also use this boilerplate but my advise would be to first learn know-how of django and user models and build a boilerplate themselves. This will help them understand why and how things are done.

## Steps to use

- Install Python( link : https://www.python.org/downloads/ ). This boilerplate uses ```python 3.8.5``` here.

- Install virtualenv ( link : https://virtualenv.pypa.io/en/latest/installation.html )

- Clone this repository. Replace YOUR PROJECT NAME with the name you want

```bash
mkdir YOUR PROJECT NAME
cd YOUR PROJECT NAME
git clone https://github.com/Priyanshu24/django-starter-boilerplate.git .
```

- Create a virtual environment in the directory in which you have cloned the repository

```bash
virtualenv -p python3 env
```

- Activate the virtual environment

```bash
source env/bin/activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Create a ```.env``` file in ```config``` folder and add the following key-value pairs.

```bash
SECRET_KEY=YOUR VALUE
DEBUG=True
```

- Replace 'YOUR VALUE' with a secret key. You can generate a secret key with the following command :

```bash
python -c "import secrets; print(secrets.token_urlsafe())"
```


The boilerplate comes with the default database configuration i.e with SQLite3. However if you intend to use complex functions and scale up your application please use some other database. My advise would be PostgreSQL or MySQL ( documentation : https://docs.djangoproject.com/en/3.1/ref/settings/#databases ). However, I prefer the former. After you configure the database or use the default one, run migrations with following commands

```bash
python manage.py makemigrations
python manage.py migrate
```

And you are done. Now you are ready to start your awesome project with custom user model.
