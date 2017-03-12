import random
from worldgen.models import *

#create the cursor and connection for the data DB

#age of npc
#related to DB. dont change
buildings=[
'inn',
'alchemist',
'blacksmith',
'jeweler',
'enchanter',
'magicweps',
'holysite',
'stables'
]

def generateBuilding(buildings=buildings):
	#reset variables
	generatedBuilding = {}
	listOfBuildings=[]
	for buildingType in Building_type.objects.all():
		generatedBuilding = {}
		generatedBuilding['type'] = buildingType
		firstName = random.choice(buildingType.building_name_first_set.all()).name
		lastName = random.choice(buildingType.building_name_last_set.all()).name
		generatedBuilding['name'] =  firstName+ " " + lastName
		listOfBuildings.insert(0,generatedBuilding)
	
	return(listOfBuildings)