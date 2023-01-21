from django.db import models
from django.contrib.auth.models import User


class Attribute(models.Model):
    character = models.CharField(max_length=20)

    def _repr_(self):
        return str(self.character)

    def _str_(self):
        return str(self.character)


# class App_user(models.Model):
#     username = models.CharField(default="", max_length=20)
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     sex = models.CharField(max_length=20)
#     self_attribute = models.CharField(default="", max_length=20)
#     partner_attribute = models.CharField(default="", max_length=20)
#
#     def _repr_(self):
#         return self.name + " " + str(self.age) + " " + self.sex + " " + self.self_attribute + " " + self.partner_attribute
#
#     def _str_(self):
#         return self.name + " " + str(self.age) + " " + self.sex + " " + self.self_attribute + " " + self.partner_attribute

class AccountHolder(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=20,blank=True)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=20,blank=True)
    self_attribute = models.CharField(default="", max_length=20)
    partner_attribute = models.CharField(default="", max_length=20)


    def _str_(self):
        return self.user.username
    def _repr_(self):
        return self.user.username