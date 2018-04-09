from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def listOfPropertyNames(self):
        listToReturn = ['Name','City']
        return listToReturn
    def listOfProperties(self):
        listToReturn = [self.name, self.city]
        return listToReturn

    class Meta:
        db_table = "CUSTOMER"

class Employee(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def listOfPropertyNames(self):
        listToReturn = ['Name','City','Age']
        return listToReturn
    def listOfProperties(self):
        listToReturn = [self.name, self.city, self.age]
        return listToReturn

    class Meta:
        db_table = "EMPLOYEE"