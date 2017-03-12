import random
from .models import *

buildings =[
"Inn",
"general Store",
"Alchemy",
"blacksmith",
"jeweler",
"enchanter",
"magic weapons",
"holysite",
"animal keeper"
]
#possible jobs in the town
#non-db related
jobs = [
"innkeep",
"Alchemist",
"blacksmith",
"jeweler",
"enchanter",
"Magic Weapons",
"General Store",
"Guard Captain",
"Holy person",
"town master",
"animal keeper",
"random1",
"random2",
"random3",
"random4",
"random5"
]
#possible genders
#related to DB. dont change
gender=[
'male',
'female'
]
#age of npc
#non-db related
age = [
'young',
'middle aged',
'old',
'very old',
'is he dead?'
]


def generateRace(requestedRace=0):
	#reset variables
	character = {}
	firstName =[]
	lastName =[]
	personality=[]
	charRace =[]
	#if user has specified a race
	if (requestedRace == 0):
		race = random.choice(Race.objects.all())
		
	else:
		race = random.choice(Race.objects.all())

	#build character details
	character['race'] = race
	character['gender'] = random.choice(gender)
	
	if character['gender'] == "male":
		character['firstName'] = random.choice(race.name_first_male_set.all())
	else:
		character['firstName'] = random.choice(race.name_first_female_set.all())

	character['lastName'] = random.choice(race.name_last_set.all())
	character['personality1'] = random.choice(Personality1.objects.all())
	character['personality2'] = random.choice(Personality2.objects.all())
	character['age'] = random.choice(age)
	return(character)


