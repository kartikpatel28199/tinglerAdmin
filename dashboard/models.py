from operator import mod
from tkinter import CASCADE
from django.db import models
from numpy import integer

# Create your models here.
class User(models.Model):

    gender_types = ((1,"Male"),(2,"Female"),(3,"Other"))

    id = models.CharField(primary_key=True,max_length=45)
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    gender = models.IntegerField(choices=gender_types)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    dateOfBirth = models.DateTimeField()
    profileLink = models.CharField(max_length=245)
    interests = models.JSONField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    deletedAt = models.DateTimeField()

    class Meta:
        db_table = 'user'
        verbose_name_plural = 'User'

    def __str__(self):
        return self.id

class UserSetting(models.Model):
    on_off = ((1,'On'),(0,'Off'))
    distance_type =(('Km','Km'),("Mi","Km"))

    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, db_column="userId" , blank=True, null=True, on_delete=models.CASCADE, verbose_name="User")
    latitude = models.CharField(max_length=45)
    longitude = models.CharField(max_length=45)
    isGlobal = models.CharField(max_length=2,db_column="global")    
    distanceRange = models.CharField(max_length=45)
    showMe = models.IntegerField(choices=on_off,default=0)
    tinglerAlert = models.IntegerField(choices=on_off,default=0)
    showProfilePic = models.IntegerField(choices=on_off,default=0)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    showActivityStatus = models.IntegerField(choices=on_off,default=0)
    distanceType = models.CharField(choices=distance_type,max_length=5)
    notification = models.CharField(max_length=45)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    deletedAt = models.DateTimeField()

    class Meta:
        db_table = 'user_setting'
        verbose_name_plural = 'User Setting'

    def __str__(self):
        return self.id

class ProfileSetting(models.Model):
    gender_types = ((1,"Male"),(2,"Female"),(3,"Other"))


    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, db_column="userId" , blank=True, null=True, on_delete=models.CASCADE, verbose_name="User")
    photosLink = models.JSONField()
    aboutMe = models.CharField(max_length=225)
    passion = models.CharField(max_length=45)
    jobTitle = models.CharField(max_length=45)
    company = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    interested = models.IntegerField(choices=gender_types)
    showGender = models.CharField(max_length=5)
    showAge = models.CharField(max_length=5)
    showDistance = models.CharField(max_length=5)
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    deletedAt = models.DateTimeField()


class UserRating(models.Model):
    id = models.AutoField(primary_key=True)
    fromUserId = models.ForeignKey(User, related_name='fromUserId' , db_column="fromUserId" , blank=True, null=True, on_delete=models.CASCADE, verbose_name="From User")
    toUserId = models.ForeignKey(User,related_name="toUserId", db_column="toUserId" , blank=True, null=True, on_delete=models.CASCADE, verbose_name="To User")
    likes = models.IntegerField()
    disLikes = models.IntegerField()
    superLikes = models.IntegerField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    deletedAt = models.DateTimeField()

    class Meta:
        db_table = 'user_Rating'
        verbose_name_plural = 'User Rating'

    def __str__(self):
        return self.id

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.JSONField()
    price = models.CharField(max_length=15)
    tingler = models.IntegerField()
    createdAt = models.DateTimeField()
    deletedAt = models.DateTimeField()

    class Meta:
        db_table = 'plan'
        verbose_name_plural = 'Plan'

    def __str__(self):
        return self.id

class PlanSubscription(models.Model):

    id= models.AutoField(primary_key=True)
    userId = models.ForeignKey(User , db_column="userId" , blank=True, null=True, on_delete=models.CASCADE)
    planId = models.ForeignKey(Plan, db_column="planId", blank=True, null=True, on_delete=models.CASCADE)
    paymentMethod = models.CharField(max_length=5)
    createdAt = models.DateTimeField()

    class Meta:
        db_table = 'plan_subscription'
        verbose_name_plural = 'Plan Subscription'

    def __str__(self):
        return self.id

