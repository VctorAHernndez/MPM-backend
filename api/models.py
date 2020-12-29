from django.db import models
from .validators import phone_shape_validator

# Create your models here.
class Provider(models.Model):
    full_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100) # standalone entity?

    def __str__(self):
        return self.full_name

class Appointment(models.Model):

    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other')
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    appointment_reason = models.TextField()

    # Create Patient Model?
    # Would be bad on flexibility because Patients
    # wouldn't be available to book appointments
    # until they've registered in the database.
    patient_full_name = models.CharField(max_length=100) # first_name or full_name (requirements)?
    patient_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    patient_date_of_birth = models.DateField()
    # TODO: Implement better validation using
    # https://stackoverflow.com/questions/14894899/what-is-the-minimum-length-of-a-valid-international-phone-number
    patient_phone_number = models.CharField(validators=[phone_shape_validator], max_length=17, blank=True)

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_full_name

# class Patient(models.Model):

#     GENDER_MALE = 'M'
#     GENDER_FEMALE = 'F'
#     GENDER_OTHER = 'O'
#     GENDER_CHOICES = (
#         (GENDER_MALE, 'Male'),
#         (GENDER_FEMALE, 'Female'),
#         (GENDER_OTHER, 'Other')
#     )

#     full_name = models.CharField(max_length=100) # split into first/middle/last names?
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     date_of_birth = models.DateField()
#     phone_number = models.CharField(validators=[phone_validator], max_length=17, blank=True)

#     # Store email so we can email back
#     # 1. if preferred appointment date is not available
#           (due to vacation, non-work day, conflict, appointment_reason),
#     # 2. if appointment date had to be changed
#     # 3.
#     email = models.EmailField()

#     def __str__(self):
#         return self.full_name
