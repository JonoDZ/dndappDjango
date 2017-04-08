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

def generateRace(seed, requestedRaces=0):
	#reset variables
	character = {}
	personality=[]
	charRace =[]
	races=[]
	random.seed(seed)
	#if user has specified a race
	if (requestedRaces == 0):
		race = random.choice(Race.objects.all())
		
	else:	
		for raceChoice in requestedRaces:
			races.insert(0,Race.objects.filter(race__startswith=raceChoice))
		race = random.choice(races)[0]
	#build character details
	character['race'] = race
	random.seed(seed)
	character['gender'] = random.choice(gender)
	
	random.seed(seed)
	
	if character['gender'] == "male":
		character['firstName'] = random.choice(race.name_first_male_set.all())
	else:
		character['firstName'] = random.choice(race.name_first_female_set.all())
	
	random.seed(seed)
	character['lastName'] = random.choice(race.name_last_set.all())
	random.seed(seed)
	character['personality1'] = random.choice(Personality1.objects.all())
	random.seed(seed)
	character['personality2'] = random.choice(Personality2.objects.all())
	#random.seed(seed)
	#character['age'] = random.choice(age)
	return(character)


