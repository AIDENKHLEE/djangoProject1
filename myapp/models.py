from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
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

class AccountHolder(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    user_visited = models.ManyToManyField(Attribute)
    # Need to check if it is right to input Attribute in this field
    def __str__(self):
        return self.user.username
    def __repr__(self):
        return self.user.username