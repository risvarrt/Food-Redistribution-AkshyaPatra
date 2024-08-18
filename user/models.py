from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    STATUS_CHOICES = (
        ('Donor', 'Donor'),
        ('Hungers(Acceptors)', 'Hungers(Acceptors)'),
        ('Volunteer', 'Volunteer'),
    )
    type_of_user = models.CharField(max_length=40,choices=STATUS_CHOICES,default='Donor',blank=True, null=True)
    NATURE_CHOICES = (
        ('CATRER', 'CATRER'),
        ('COMPANY', 'COMPANY'),
        ('COLLEGE', 'COLLEGE'),
        ('SCHOOL', 'SCHOOL'),
        ('FACTORY', 'FACTORY'),
        ('HOSTEL', 'HOSTEL'),
    )
    nature_of_institution = models.CharField(max_length=20,choices=NATURE_CHOICES,default='CATRER',blank=True, null=True)
    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name_of_institution = models.CharField(null=True,max_length=100,blank=True)
    your_role = models.CharField(null=True,max_length=100,blank=True)
    address = models.CharField(null=True,max_length=100,blank=True)
    city = models.CharField(null=True,max_length=100,blank=True)
    mobile_no = models.IntegerField(blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    does_it_have_kitchen = models.BooleanField(null=True)
    premium_accout = models.BooleanField(null=True)
    does_it_accept_raw_food = models.BooleanField(null=True)
    latitude = models.CharField(null=True,max_length=100,blank=True)
    longitude = models.CharField(null=True,max_length=100,blank=True)
    PRE_CHOICES = (
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg'),
        ('Veg/Nonveg', 'Veg/Nonveg'),
    )
    please_specify_food_perference = models.CharField(max_length=40,choices=PRE_CHOICES,default='Veg',blank=True, null=True)
    REG_CHOICES = (
        ('Govt support entity(Registered)', 'Govt support entity(Registered)'),
        ('Non Govt support entity(Registered)', 'Non Govt support entity(Registered)'),
        ('Individual led charitable(Unregistered)', 'Individual led charitable(Unregistered)'),
        ('Unorganized Space(Unregistered)','Unorganized Space(Unregistered)'),
        ('Others','Others'),
    )
    status_of_registration = models.CharField(max_length=40,choices=REG_CHOICES,default='Govt support entity(Registered)',blank=True, null=True)
    PRE1_CHOICES = (
        ('Volunteer', 'Volunteer'),
        ('Work On Technology Platform', 'Work On Technology Platform'),
    )
    how_would_you_like_to_help = models.CharField(max_length=40,choices=PRE1_CHOICES,default='Volunteer',blank=True, null=True)

    any_thing_would_you_like_to_tell_us = models.CharField(null=True,max_length=100,blank=True)

    def __str__(self):
        return f'{ self.user.username} Profile'
