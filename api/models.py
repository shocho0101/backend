from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, _user_has_perm)
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, request_data):
        if not request_data["userID"]:
            raise ValueError("userID must be set")

        if not request_data["username"]:
            raise  ValueError("username must be set")


        user = self.model(
            username = request_data["username"],
            userID = request_data["userID"],
            loginType = request_data["loginType"])
        user.set_password(request_data["password"])
        user.save(using= self._db)
        return user

    def create_superuser(self, userID, username, password, loginType):
        request_data = {
            "username" : username,
            "userID" : userID,
            "password" : password,
            "loginType" : loginType
        }
        user = self.create_user(request_data)

        user.is_admin = True
        user.save(using = self._db)

class Account(AbstractBaseUser):
    userID = models.CharField(_("userID"), max_length=255, unique=True)
    username = models.CharField(_("username"), max_length=20)
    loginType = models.CharField(_("loginType"), max_length= 20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = AccountManager()

    USERNAME_FIELD = "userID"
    REQUIRED_FIELDS = ["loginType", "username"]

    def user_has_perm(user, perm, obj):
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_short_name(self):
        return self.username

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return  self.is_admin

class Group(models.Model):
    name = models.CharField(max_length=255)
    member = models.ManyToManyField(Account, related_name= "Groups")
    joincode = models.CharField(max_length= 255)

class Homework(models.Model):
    name = models.CharField(max_length=255)
    deadline = models.DateField()
    group = models.ForeignKey(Group, related_name="homeworks")
