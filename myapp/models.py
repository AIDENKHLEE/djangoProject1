from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(default="", max_length=20)
    age = models.IntegerField(default=0, max_length=20)
    sex = models.CharField(max_length=20)
    self_attribute = models.CharField(default="", max_length=20)
    partner_attribute = models.CharField(default="", max_length=20)

    def __repr__(self):
        return self.name + " " + str(self.age) + " " + self.sex + " " + self.self_attribute + " " + self.partner_attribute

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.sex + " " + self.self_attribute + " " + self.partner_attribute


class Attribute(models.Model):
    character = models.CharField(max_length=20)

    def __repr__(self):
        return str(self.character)

    def __str__(self):
        return str(self.character)

from django.db import models
from django.contrib.auth.models import User

class AccountHolder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=20)
    age = models.IntegerField(default=0, max_length=20)
    sex = models.CharField(default="", max_length=20)
    self_attribute = models.CharField(default="", max_length=20)
    partner_attribute = models.CharField(default="", max_length=20)

    def _repr_(self):
        return self.user.username + " " + self.name + " " + str(self.age) + " " + self.sex + " " + self.self_attribute + " " + self.partner_attribute

    def _str_(self):
        return self.user.username + " " + self.name + " " + str(self.age) + " " + self.sex + " " + self.self_attribute + " " + self.partner_attribute


class Attribute(models.Model):
    character = models.CharField(max_length=20)

    def _repr_(self):
        return str(self.character)

    def _str_(self):
        return str(self.character)