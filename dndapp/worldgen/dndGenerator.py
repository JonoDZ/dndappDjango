import worldgen.charGen as charGen
import worldgen.buildingGen as buildingGen
from worldgen.generators import *
import random


def genChar(chars=0, toGen=10, seed=0):
	charlist =[]
	#generate seed if not supplied
	if seed == 0:
		seed = random.random()

	#set the seed, then, generate npc seed1s
	random.seed(seed)
	npcGenSeeds = [random.random() for _ in range(toGen)]

	if chars == 0 or not chars:	
		for i, NpcSeed in enumerate(npcGenSeeds):
			charlist.insert(0,(charGen.generateRace(NpcSeed)))
	else:	
		for i, NpcSeed in enumerate(npcGenSeeds):
			charlist.insert(0,(charGen.generateRace(NpcSeed, chars)))
	return charlist

def genBuilding(buildings=0):
	buildingList =[]
	buildingList = buildingGen.generateBuilding()
	return buildingList

def genDrinks(seed=0):
	if seed == 0:
		seed = random.random()

	drinkList =[]
	drinkList = generateDrinks(seed)
	return drinkList