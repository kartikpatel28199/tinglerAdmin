from django.contrib import admin

from dashboard.models import Plan, PlanSubscription, ProfileSetting, User, UserRating, UserSetting

# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    readonly_fields = ["firstName","lastName","gender","phone","email","dateOfBirth","profileLink","interests","createdAt","updatedAt","deletedAt"]
    list_display = ("id","firstName","lastName","gender","phone","email","dateOfBirth","profileLink","interests","createdAt","updatedAt","deletedAt")

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(UserSetting)
class UserSetting(admin.ModelAdmin):
    readonly_fields = ["userId","latitude","longitude","isGlobal","distanceRange","showMe","tinglerAlert","showProfilePic","age_min","age_max","showActivityStatus","distanceType","notification","createdAt","updatedAt","deletedAt"]
    list_display = ("id","userId","latitude","longitude","isGlobal","distanceRange","showMe","tinglerAlert","showProfilePic","age_min","age_max","showActivityStatus","distanceType","notification","createdAt","updatedAt","deletedAt")

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(ProfileSetting)
class ProfileSetting(admin.ModelAdmin):
    readonly_fields = ["userId","photosLink","aboutMe","passion","jobTitle","company","school","city","interested","showGender","showAge","showDistance","createdAt","updatedAt","deletedAt"]
    list_display = ("id","userId","photosLink","aboutMe","passion","jobTitle","company","school","city","interested","showGender","showAge","showDistance","createdAt","updatedAt","deletedAt")

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
@admin.register(UserRating)
class UserRating(admin.ModelAdmin):
    readonly_fields = ["toUserId","fromUserId","likes","disLikes","superLikes","createdAt","updatedAt","deletedAt"]
    list_display = ("id","toUserId","fromUserId","likes","disLikes","superLikes","createdAt","updatedAt","deletedAt")

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Plan)
class Plan(admin.ModelAdmin):
    readonly_fields = ["name","description","price","tingler","createdAt","deletedAt"]
    list_display = ("id","name","description","price","tingler","createdAt","deletedAt")

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(PlanSubscription)
class PlanSubscription(admin.ModelAdmin):
    readonly_fields = ["userId","planId","paymentMethod","createdAt"]
    list_display = ("id","userId","planId","paymentMethod","createdAt")

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
