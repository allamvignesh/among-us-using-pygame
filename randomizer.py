import random

wiring = [5, 10, 17, 42, 37, 25, 31]
powerTo = [36, 34, 2, 15, 11, 17, 6, 30]
dowloadable = [4, 1, 12, 19, 23]
garbage = [3, 9]
tasks = [0, 14, 13, 16, 45, 43]
comp = [40, 8, 26]

def getWiring():
	return [[random.choice(wiring)]]

def getPowerTo():
	return [[24, random.choice(powerTo)]]

def getDownload():
	return [[random.choice(dowloadable), 38]]

def getChoice():
	x = random.choice([0, 1, 2])
	if x == 0:
		return [['Fual engines', 21, 35, 21, 32]]
	elif x == 1:
		return [['Allign Engines', 49, 33]]
	else:
		return [['MedBay', random.choice([28, 27])]]

def getGarbage():
	if random.choice([True, False]):
		return [['Empty Garbage', random.choice(garbage), 20]]
	else:
		return [[random.choice(tasks)]]

def getComp():
	return [[random.choice(comp)]]

def getAllTasks():
	AllTasks = getWiring() + getPowerTo() + getDownload() + getChoice() + getGarbage() + getComp()
	return AllTasks