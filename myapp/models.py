from django.db import models



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

