from django.db import models

################
################
##### NPCS #####
################
################

##### RACES ####
class Race(models.Model):
    race = models.CharField(max_length=15)
    def __str__(self):
        return self.race

class Gender(models.Model):
    gender = models.CharField(max_length=8)
    def __str__(self):
        return self.gender

class Personality1(models.Model):
    personailty = models.CharField(max_length=40)
    def __str__(self):
        return self.personailty

class Personality2(models.Model):
    personailty = models.CharField(max_length=40)
    def __str__(self):
        return self.personailty

class Appearance(models.Model):
    Appearance = models.CharField(max_length=40)
    def __str__(self):
        return self.Appearance

class Name_first_male(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Name_first_female(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Name_last(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

################
################
## BUILDINGS ###
################
################

class Building_type(models.Model):
    buildingType = models.CharField(max_length=40)
    def __str__(self):
        return self.buildingType

class Building_name_first(models.Model):
    building_type = models.ForeignKey(Building_type, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Building_name_last(models.Model):
    building_type = models.ForeignKey(Building_type, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name