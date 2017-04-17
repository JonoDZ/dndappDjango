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

################
################
### OBJECTS ####
################
################

## DRINK ##
class Drink_name(models.Model):
    drinkName = models.CharField(max_length=60)
    def __str__(self):
        return self.drinkName
        
class Drink_type(models.Model):
    drinkType = models.CharField(max_length=20)
    def __str__(self):
        return self.drinkType

## DRUGS ##
class Drug_name(models.Model):
    drugName = models.CharField(max_length=20)
    def __str__(self):
        return self.drinkType

class Drug_type(models.Model):
    drugType = models.CharField(max_length=20)
    def __str__(self):
        return self.drinkType

class Physical_affect_1(models.Model):
    physAff = models.CharField(max_length=50)
    def __str__(self):
        return self.drinkType

class Physical_affect_2(models.Model):
    physAff = models.CharField(max_length=20)
    def __str__(self):
        return self.drinkType

class Emotion(models.Model):
    emotion = models.CharField(max_length=20)
    def __str__(self):
        return self.drinkType

class Strength(models.Model):
    strength = models.CharField(max_length=20)
    def __str__(self):
        return self.drinkType

## ITEMS ##

class Weapon_properties(models.Model):
    weaponProperty = models.CharField(max_length=20)
    def __str__(self):
        return self.weaponProperty

class Weapon_damage_type(models.Model):
    weaponDamageType = models.CharField(max_length=20)
    def __str__(self):
        return self.weaponDamageType

class Item_gear(models.Model):
    shops = models.ManyToManyField(Building_type)
    name = models.CharField(max_length=40)
    weight = models.IntegerField()
    costCopper = models.IntegerField()
    costSilver = models.IntegerField()
    costGold = models.IntegerField()
    def __str__(self):
        return self.name

class Item_weapon(models.Model):
    shops = models.ManyToManyField(Building_type)
    name = models.CharField(max_length=40)
    costCopper = models.IntegerField(default=0)
    costSilver = models.IntegerField(default=0)
    costGold = models.IntegerField(default=0)
    damageDieQuant = models.IntegerField()
    damageDieType = models.IntegerField()
    damageType = models.ForeignKey(Weapon_damage_type, on_delete=models.CASCADE)
    weight = models.IntegerField()
    weaponRangeMin = models.IntegerField(default=0)
    weaponRangeMax = models.IntegerField(default=0)
    weaponProperties = models.ManyToManyField(Weapon_properties)
    def __str__(self):
        return self.name

