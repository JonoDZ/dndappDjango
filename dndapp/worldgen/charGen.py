import random
from .models import *
#create the cursor and connection for the data DB
#
#VARIABLES
#

#possible builds in the town. 
#non-db related
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

#lastestHumanNames = Human_male_name.objects.order_by('name')


#get all items from alist in DB
"""
def getItemsFromDb(item, table, connCursor=c):
	returnList = []
	for row in connCursor.execute('SELECT '+item+' FROM '+table+''):
			if row[0] != None:
				returnList.insert(0,row[0])
	return returnList
	"""
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
		character['race'] = random.choice(Race.objects.all())

	#build character details
	character['race'] = race
	character['gender'] = random.choice(gender)
	character['lastName'] = random.choice(age)
	character['firstName'] = random.choice(Human_male_name.objects.all())
	character['personality1'] = random.choice(jobs)
	character['personality2'] = random.choice(buildings)
	character['age'] = random.choice(age)
	#get all personality 1 types
	#get all personality 2 tyoes
	#a random data from generated lists, apply to character.

	return(character)


