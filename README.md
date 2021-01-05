# Medical Provider Marketplace

This project is a prototype version of a Medical Provider Marketplace where people can find a doctor or other healthcare provider to book an appointment with. Users are able to search the marketplace for providers, see a list of all medical providers, and select a provider to book an appointment with. Inspired on a similar concept called [Zocdoc](https://www.zocdoc.com).

[Click here](https://mpm-django-backend.herokuapp.com) for the live demo.

# Usage

1. Clone repository
2. `cd` into the cloned folder
3. Create a virtual environment (`python -m venv env`)
4. Activate the virtual environment (`source env/bin/activate`)
5. Install requirements (`pip install -r requirements`)
6. Create an `.env` file to store important credentials:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
```

7. Make migrations

  - `python manage.py makemigrations api`
  - `python manage.py migrate`

8. Create app superuser (`python manage.py createsuperuser`)
9. Start server (`python manage.py runserver`)

Alternatively, you can start the server with [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) using the command `heroku local`, but make sure to run `python manage.py collectstatic` first!

### For Mac Users

Installation of `psycopg2` might be cumbersome if built from source. You might want to check out [this post](https://stackoverflow.com/questions/9678408/cant-install-psycopg2-with-pip-in-virtualenv-on-mac-os-x-10-7). Alternatively, you might want to simply install the binary itself (already included in `requirements.txt` as `psycopg2-binary`).

### Additional Notes

If you would like to run it on production (which uses PostgreSQL), you would have to make changes in `.env`, explicitly setting `DEBUG` to `False` and adding the `DB_USER`, `DB_NAME`, `DB_PASSWORD`, `DB_HOST` and `DB_PORT` variables. Make sure to create the appropriate PostgreSQL roles with login permissions.

# Progress & Maintenance

The build and maintenance progress is being documented [here](https://trello.com/b/u6mFQulW/medical-provider-marketplace), for anyone interested.

# Acknowledgements

This project was bootstrapped with [Django Admin](https://docs.djangoproject.com/en/3.1/ref/django-admin/).
