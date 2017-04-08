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