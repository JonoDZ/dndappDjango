from django.db import models

### RACES ###
### RACES ##
class Race(models.Model):
    race = models.CharField(max_length=15)
    def __str__(self):
        return self.race

################
#### TRAITS ####
##### AND ######
## APPEARANCE ##
################

class Personailty1(models.Model):
    personailty = models.CharField(max_length=40)
    def __str__(self):
        return self.personailty

class Personailty2(models.Model):
    personailty = models.CharField(max_length=40)
    def __str__(self):
        return self.personailty

class Appearance(models.Model):
    Appearance = models.CharField(max_length=40)
    def __str__(self):
        return self.Appearance

################
################
## BUILDINGS ###
################
################


################
################
#### NAMES #####
################
################

### HUMAN ###

class Human_male_name(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Human_female_name(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Human_last_name(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

### GNOME ###

class Gnome_male_name(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Gnome_female_name(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Gnome_last_name(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Orc_male_name(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Name_first(object):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name