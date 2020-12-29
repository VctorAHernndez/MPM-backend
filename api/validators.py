from django.core.validators import RegexValidator

# Taken from:
# https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
