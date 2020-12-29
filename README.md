# Medical Provider Marketplace

This project is a prototype version of a Medical Provider Marketplace where people can find a doctor or other healthcare provider to book an appointment with. Users are able to search the marketplace for providers, see a list of all medical providers, and select a provider to book an appointment with. Inspired on a similar concept called [Zocdoc](https://www.zocdoc.com).

# Usage

1. Clone repository
2. `cd` into the cloned folder
3. Create a virtual environment (`python -m venv env`)
4. Activate the virtual environment (`source env/bin/activate`)
5. Install requirements (`pip install -r requirements`)
6. Create an `.env` file to store important credentials:

```
SECRET_KEY=very-secrety
```

7. Make migrations

  - `python manage.py migrate`
  - `python manage.py makemigrations`

8. Create app superuser (`python manage.py createsuperuser`)
9. Start server (`python manage.py runserver`)

# Progress & Maintenance

The build and maintenance progress is being documented [here](https://trello.com/b/u6mFQulW/medical-provider-marketplace), for anyone interested.

# Acknowledgements

This project was bootstrapped with [Django Admin](https://docs.djangoproject.com/en/3.1/ref/django-admin/).
