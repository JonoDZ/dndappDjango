import random
from .models import *


def generateDrinks(seed):
	#reset variables
	drinksList = []
	random.seed(seed)
	drinkNameList = Drink_name.objects.all()
	for drinkType in Drink_type.objects.all():
		drink = ""
		drink = drink + getattr(random.choice(drinkNameList),'drinkName') + " " + getattr(drinkType, 'drinkType')
		drinksList.insert(0, drink)

	return(drinksList)

def generateDrugs(seed):
	drug = {}
	drugsList =[]
	random.seed(seed)
	for drugType in Drug_type.objects.all():
		drug['type'] = drugType
		drug['name'] = random.choice(Drug_name.objects.all())
		drug['physAff1'] = random.choice(Physical_affect_1.objects.all())
		drug['physAff2'] = random.choice(Physical_affect_2.objects.all())
		drug['emotion'] = random.choice(Emotion.objects.all())
		drug['strength'] = random.choice(Strength.objects.all())
		drugsList.insert(0,drug)
	return	drugsList