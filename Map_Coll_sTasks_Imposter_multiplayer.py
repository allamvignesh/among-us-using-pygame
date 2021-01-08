import pygame
from pygame.locals import *
from walk_anim import Player
import pickle
from Tasks import Tasks
from threading import Thread
from randomizer import getAllTasks
from networking.client import client

connect = client()

life = eval(connect.send((0, 0, 1, 0, (0, 0, 0), False, False)))
ownpos = eval(life[str(f"b'{connect.name}'")])[-2]
imposter = eval(life[str(f"b'{connect.name}'")])[6]

My_color = eval(input('Enter ur color: '))
pygame.init()

clock = pygame.time.Clock()
fps = 60
size =[1000, 550]
screen = pygame.display.set_mode(size)
screen.set_colorkey('#000000')

AllTasks = getAllTasks()

font_size = 18
font = pygame.font.Font('freesansbold.ttf', font_size)

Text1 = 'fixWiring '

Text2 = 'divert and accept power '

Text3 = 'Download and Upload '

Text4 = f'{AllTasks[3][0]} '
if str(AllTasks[4][0])[0].isalpha():
	Text5 = f'{AllTasks[4][0]} '
else:
	Text5 = 'Usual Tasks '

Text6 = 'Main Tasks '

for i in range(len(AllTasks)):
	for j in range(len(AllTasks[i])):
		if str(AllTasks[i][j])[0].isalpha():
			print(AllTasks[i][j])
			del AllTasks[i][j]
			break
print(AllTasks)
tasksToDo = None

a = 0
b = 0
c = 0

cam_on = pygame.image.load("models/map parts/cam-on.png")
cam_off = pygame.image.load("models/map parts/cam-off.png")
redirect = pygame.image.load("models/map parts/redirect.png")
electric = pygame.image.load("models/map parts/electric.png")
upload = pygame.image.load("models/map parts/weapons/upload.png")
vent_pic = pygame.image.load("models/map parts/vent.png")

#cafeteria
bg = pygame.image.load('models/map parts/PC Computer - Among Us - Skeld Cafeteria.png')
caflev = pygame.transform.flip(pygame.image.load("models/map parts/oxygen/o2-4.png"), True, False)
cafup = upload
cafred = pygame.transform.flip(pygame.image.load("models/map parts/weapons/redirect.png"), True, False)

#weapons
caf_weap = pygame.image.load("models/map parts/weapons/caf-weapons.png")
weapons1 = pygame.image.load("models/map parts/weapons/weapons-1.png")
weapons2 = pygame.image.load("models/map parts/weapons/weapons-2.png")
weapons3 = pygame.image.load("models/map parts/weapons/weapons-3.png")
weapons4 = pygame.image.load("models/map parts/weapons/weapons-4.png")
weapons5 = pygame.image.load("models/map parts/weapons/weapons-5.png")
weapons6 = pygame.image.load("models/map parts/weapons/weapons-6.png")
weapons7 = pygame.image.load("models/map parts/weapons/weapons-7.png")
weapons8 = pygame.image.load("models/map parts/weapons/weapons-8.png")
weapons9 = pygame.image.load("models/map parts/weapons/weapons-9.png")
weapons10 = pygame.image.load("models/map parts/weapons/weapons-10.png")
weaponselectric = pygame.image.load("models/map parts/weapons/redirect.png")
weaponsupload = upload
weaponsgreenscreen = pygame.image.load("models/map parts/weapons/greenscreen.png")

#oxygen
wep_o2_nav_she = pygame.image.load("models/map parts/oxygen/wep-ox-nav-she.png")
o21 = pygame.image.load("models/map parts/oxygen/o2-1.png")
o22 = pygame.image.load("models/map parts/oxygen/o2-2.png")
o23 = pygame.image.load("models/map parts/oxygen/o2-3.png")
o24 = pygame.image.load("models/map parts/oxygen/o2-4.png")
o25 = pygame.image.load("models/map parts/oxygen/o2-5.png")
o26 = pygame.image.load("models/map parts/oxygen/o2-6.png")
o27 = pygame.image.load("models/map parts/oxygen/o2-7.png")
oredirect = redirect
#navigation
nav1 = pygame.image.load("models/map parts/navigation/nav-1.png")
nav2 = pygame.image.load("models/map parts/navigation/nav-2.png")
nav3 = pygame.image.load("models/map parts/navigation/nav-3.png")
nav4 = pygame.image.load("models/map parts/navigation/nav-4.png")
nav5 = pygame.image.load("models/map parts/navigation/nav-5.png")
nav6 = pygame.image.load("models/map parts/navigation/nav-6.png")
nav7 = pygame.image.load("models/map parts/navigation/nav-7.png")
nav8 = pygame.image.load("models/map parts/navigation/nav-8.png")
nav9 = pygame.image.load("models/map parts/navigation/nav-9.png")
navredirect = redirect
navelectric = electric

#admin
caf_ad_st = pygame.image.load("models/map parts/admin/admin-4.png")
admin1 = pygame.image.load("models/map parts/admin/admin-1.png")
admin2 = pygame.image.load("models/map parts/admin/admin-2.png")
admin3 = pygame.image.load("models/map parts/admin/admin-3.png")
admin4 = pygame.image.load("models/map parts/admin/admin-5.png")
admin5 = pygame.image.load("models/map parts/admin/admin-6.png")
admin6 = pygame.image.load("models/map parts/admin/admin-7.png")
admin7 = pygame.image.load("models/map parts/admin/admin-8.png")
admin8 = pygame.image.load("models/map parts/admin/admin-9.png")
admin9 = pygame.image.load("models/map parts/admin/admin-10.png")
admin10 = pygame.image.load("models/map parts/admin/admin-10.png")
adminelec = electric
adminupl = upload
adminox = o23

#storage
sto1 = pygame.image.load("models/map parts/storage/storage-1.png")
sto2 = pygame.image.load("models/map parts/storage/storage-2.png")
sto3 = pygame.image.load("models/map parts/storage/storage-3.png")
sto4 = pygame.image.load("models/map parts/storage/storage-4.png")
sto5 = pygame.image.load("models/map parts/storage/storage-5.png")
sto6 = electric
sto7 = pygame.image.load("models/map parts/storage/storage-7.png")

#commnication
comm1 = pygame.image.load("models/map parts/communication/comm-1.png")
comm2 = pygame.image.load("models/map parts/communication/comm-2.png")
comm3 = pygame.image.load("models/map parts/communication/comm-3.png")
comm4 = pygame.image.load("models/map parts/communication/comm-4.png")
comm5 = pygame.image.load("models/map parts/communication/comm-5.png")
comm6 = pygame.image.load("models/map parts/communication/comm-6.png")
comm7 = pygame.image.load("models/map parts/communication/comm-7.png")
comm8 = pygame.image.load("models/map parts/communication/comm-8.png")
comm9 = pygame.image.load("models/map parts/communication/comm-9.png")
comm10 = electric
comm11 = upload

#electric
ele1 = pygame.image.load("models/map parts/electric/ele-1.png")
ele2 = pygame.image.load("models/map parts/electric/ele-2.png")
ele3 = pygame.image.load("models/map parts/electric/ele-3.png")
ele4 = pygame.image.load("models/map parts/electric/ele-4.png")
ele5 = pygame.image.load("models/map parts/electric/ele-5.png")
ele6 = pygame.image.load("models/map parts/electric/ele-6.png")
ele7 = electric
ele8 = redirect
ele9 = upload

#lowerengine
low1 = pygame.image.load("models/map parts/engine/eng-1.png")
low2 = pygame.image.load("models/map parts/engine/eng-2.png")
low3 = pygame.image.load("models/map parts/engine/eng-3.png")
low4 = pygame.image.load("models/map parts/engine/eng-4.png")
low5 = pygame.image.load("models/map parts/engine/eng-5.png")
low6 = pygame.image.load("models/map parts/engine/eng-6.png")
low7 = pygame.image.load("models/map parts/engine/eng-7.png")
low8 = pygame.image.load("models/map parts/engine/eng-8.png")
low9 = pygame.image.load("models/map parts/engine/eng-10.png")
low10 = pygame.image.load("models/map parts/engine/eng-11.png")
low11 = pygame.image.load("models/map parts/engine/eng-12.png")
low12 = pygame.image.load("models/map parts/engine/eng-13.png")
low13 = pygame.image.load("models/map parts/engine/eng-9.png")
lowred = redirect

#security
sec1 = pygame.image.load("models/map parts/security/sec-1.png")
sec2 = pygame.image.load("models/map parts/security/sec-2.png")
sec3 = pygame.image.load("models/map parts/security/sec-3.png")
sec4 = pygame.image.load("models/map parts/security/sec-4.png")
sec5 = pygame.image.load("models/map parts/security/sec-5.png")
sec6 = pygame.image.load("models/map parts/security/sec-6.png")
secele = electric

#medbay
med1 = pygame.image.load("models/map parts/medbay/med-1.png")
med2 = pygame.image.load("models/map parts/medbay/med-2.png")
med3 = pygame.image.load("models/map parts/medbay/med-3.png")
med4 = pygame.image.load("models/map parts/medbay/med-4.png")

#shields
she1 = pygame.image.load("models/map parts/shields/she-1.png")
she2 = pygame.image.load("models/map parts/shields/she-2.png")
she3 = pygame.image.load("models/map parts/shields/she-3.png")
she4 = pygame.image.load("models/map parts/shields/she-4.png")
she5 = pygame.image.load("models/map parts/shields/she-5.png")
she6 = pygame.image.load("models/map parts/shields/she-6.png")
she7 = pygame.image.load("models/map parts/shields/she-7.png")
she8 = pygame.image.load("models/map parts/shields/she-8.png")
she9 = pygame.image.load("models/map parts/shields/she-9.png")
she10 = redirect

#reactor
rec1 = pygame.image.load("models/map parts/reactor/rec-1.png")
rec2 = pygame.image.load("models/map parts/reactor/rec-2.png")
rec3 = pygame.image.load("models/map parts/reactor/rec-3.png")

class Sprite(pygame.sprite.Sprite):
	def __init__(self, sizex = 10, sizey = 10, surface = 'default'):
		pygame.sprite.Sprite.__init__(self)
		if surface == 'default':
			self.image = pygame.Surface((sizex, sizey))
			self.image.fill((255, 0, 0))
		else:
			self.image = surface
		self.rect = self.image.get_rect()

q = open('collision_points.dat', 'rb')

coll_loc = pickle.load(q)

collision = [Sprite(k, l) for i,j,k,l in coll_loc]
player = Player()
players = pygame.sprite.Group()
players.add(player)

wall_group = pygame.sprite.Group()

for i in range(len(collision)):
	wall_group.add(collision[i])

topos = []
sps = []

#buttons
tasks = Sprite(surface = pygame.image.load("models/buttons/tasks.png"))
taskson = pygame.image.load("models/buttons/tasks.png")
tasksoff = pygame.image.load("models/buttons/tasks_off.png")
report = Sprite(surface = pygame.image.load("models/buttons/report.png"))
reporton = pygame.image.load("models/buttons/report.png")
reportoff = pygame.image.load("models/buttons/report_off.png")
sabotage = Sprite(surface = pygame.image.load("models/buttons/sabotage.png"))
vent = Sprite(surface = pygame.image.load("models/buttons/vent.png"))
kill = Sprite(surface = pygame.image.load("models/buttons/kill.png"))
killon = pygame.image.load("models/buttons/kill.png")
killoff = pygame.image.load("models/buttons/kill_off.png")
security = Sprite(surface = pygame.image.load("models/buttons/security.png"))
mapbut = Sprite(surface = pygame.image.load("models/buttons/map.png"))
mousebut = Sprite()

mousebut.rect.x, mousebut.rect.y = 0, 0

tasks.rect.x, tasks.rect.y = 897, 446
report.rect.x, report.rect.y = 892, 333
sabotage.rect.x, sabotage.rect.y = 897, 446
vent.rect.x, vent.rect.y = 897, 446
kill.rect.x, kill.rect.y = 789, 444
security.rect.x, security.rect.y = 789, 444
mapbut.rect.x, mapbut.rect.y = 929, 74

button_group = pygame.sprite.Group()
button_group.add(tasks)
button_group.add(report)
button_group.add(sabotage)
button_group.add(vent)
button_group.add(kill)
button_group.add(security)
button_group.add(mapbut)

but = [tasks, report, sabotage, vent, kill]
mous_grp = pygame.sprite.Group()
mous_grp.add(mousebut)

if imposter:
	tasks.rect.x, tasks.rect.y = (0, -200)
	vent.rect.x, vent.rect.y = 0, -200
	#tasksoff.rect.x, tasksoff.rect.y = (0, -200)
else:
	sabotage.rect.x, sabotage.rect.y = 0, -200
	kill.rect.x, kill.rect.y = 0, -200
	vent.rect.x, vent.rect.y = 0, -200

tskpos = [(1290, 405, 10, 10), (1290, 233, 10, 10), (1478, 397, 10, 10), (920, 256, 10, 10), (841, 180, 10, 10), (117, 121, 10, 10),
			(1260, 787, 10, 10), (1107, 817, 10, 10), (1035, 827, 10, 10), (964, 860, 10, 10), (1761, 919, 10, 10), (1878, 791, 10, 10), (1967, 776, 10, 10), (2028, 811, 10, 10), (2073, 1021, 10, 10),
			(1409, 1422, 10, 10), (1176, 1769, 10, 10), (1056, 1760, 10, 10), (922, 1972, 10, 10), (887, 1771, 10, 10), (612, 1981, 10, 10), (254, 1724, 10, 10), (-256, 1432, 10, 10), (-266, 1201, 10, 10), (-206, 1201, 10, 10), (-111, 1201, 10, 10), (54, 1201, 10, 10),
			(-67, 997, 10, 10), (-13, 936, 10, 10), (-518, 815, 10, 10), (-475, 833, 10, 10), (-719, 956, 10, 10), (-990, 1626, 10, 10), (-1007, 1617, 10, 10), (-978, 1330, 10, 10), (-1001, 588, 10, 10), (-917, 284, 10, 10),
			(639, 1091, 10, 10), (738, 1072, 10, 10), (808, 1265, 10, 10), (1012, 1265, 10, 10), (1078, 1088, 10, 10), (362, 1294, 10, 10),
			(-1316, 1020, 10, 10), (-1156, 799, 10, 10), (-1366, 710, 10, 10), (-1273, 648, 10, 10), (-1278, 1344, 10, 10), (340, 402, 220, 150), (-1071, 610, 10, 10)]


ToDo = {5:1, 4:3, 3:2, 0:9, 1:3, 2:18, 6:18, 8:5, 9:2, 10:1, 11:18, 12:3, 13:8, 14:15, 15:18, 16:14,
		17:18, 19:3, 21:12, 20:2, 42:1, 23:3, 24:10, 25:1, 26:7, 32:11, 33:6, 34:18, 43:17, 45:16, 
		31:1, 30:18, 35:11, 36:18, 27:19, 28:13, 37:1, 38:4, 40:0, 49:6}
#print(len(ToDo))
DoTo = []

taskmgr = [Sprite(k+40, l+40) for i,j,k,l in tskpos]

task_group = pygame.sprite.Group()

for i in range(len(taskmgr)):
	task_group.add(taskmgr[i])

f = []
Tasks = Tasks()

#secCam
secCam = 0
secC1 = pygame.image.load("models/tasks/Security Camera/sec-2.png")
secC2 = pygame.image.load("models/tasks/Security Camera/sec-1.png")
secC3 = pygame.image.load("models/tasks/Security Camera/sec-3.png")
secCNum = 1

#maps
show_map = False
map1 = pygame.image.load("models/maps/1.png")

#deadpos
dead = []

#alive player position
Player_Pos = []
killed_player_index = None
DeadPlayers = []
AmIDEAD = False
DEADPOS = []
other_players_group = pygame.sprite.Group()
in_vent = False
near_vent = False
in_vent_time = 0

def colorchanger(surface, color):
	"""Fill all pixels of the surface with color, preserve transparency."""
	surface = surface.convert_alpha()
	w, h = surface.get_size()
	r, g, b = color
	for x in range(w):
		for y in range(h):
			if surface.get_at((x,y)) == (255, 0, 0, 255):
				surface.set_at((x, y), pygame.Color(r, g, b, 255))
	return surface

while True:

	c += 1
	wall_group.draw(screen)
	mousebut.rect.x, mousebut.rect.y = pygame.mouse.get_pos()
	mous_grp.draw(screen)
	other_players_group.draw(screen)

	screen.fill((0, 0, 0))

	before_pos = a, b

	oo = []
	for i in AllTasks:
		if len(i) != 0:
			oo.append(i[0])
		else:
			oo.append(-10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			connect.send("disconnect")
			print(f)
			##print('\n\n', tskpos)
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			#print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
			print(pygame.mouse.get_pos()[0]-a, pygame.mouse.get_pos()[1]-b)
			#print(a, b)

			#print(a, b)

			f.append(pygame.mouse.get_pos())

			if vent.rect.colliderect(mousebut.rect):
				in_vent = not in_vent


			#f.append((pygame.mouse.get_pos()[0]-a, pygame.mouse.get_pos()[1]-b, 10, 10))

			#divertTo

			divert_To = {36:0, 34:1, 2:2, 15:3, 11:4, 6:5, 30:6}

			for i in range(len(but)):
				smashhit = pygame.sprite.collide_rect(mousebut, but[i])
				if smashhit and pygame.mouse.get_pressed()[0]:
					#print(oo)
					if tasksToDo in ToDo and not imposter and tasksToDo in oo:
						score = 0
						if ToDo[tasksToDo] == 0:
							score = Tasks.swipeCard()
						elif ToDo[tasksToDo] == 1:
							score = Tasks.fixWiring()
						elif ToDo[tasksToDo] == 2:
							score = Tasks.emptyGarbage()
						elif ToDo[tasksToDo] == 3:
							score = Tasks.upload()
						elif ToDo[tasksToDo] == 4:
							score = Tasks.Download(1)
						elif ToDo[tasksToDo] == 5:
							score = Tasks.clearLeaves()
						elif ToDo[tasksToDo] == 6:
							score = Tasks.alignEngine()
						elif ToDo[tasksToDo] == 7:
							score = Tasks.calibrate()
						elif ToDo[tasksToDo] == 8:
							score = Tasks.chartCourse()
						elif ToDo[tasksToDo] == 9:
							score = Tasks.weapons()
						elif ToDo[tasksToDo] == 10:
							score = Tasks.divertPower(divert_To[AllTasks[1][1]])
						elif ToDo[tasksToDo] == 11:
							score = Tasks.fualEngine()
						elif ToDo[tasksToDo] == 12:
							score = Tasks.fillCan()
						elif ToDo[tasksToDo] == 13:
							score = Tasks.inspectSample()
						elif ToDo[tasksToDo] == 14:
							score = Tasks.primeShield()
						elif ToDo[tasksToDo] == 15:
							score = Tasks.stabSteering()
						elif ToDo[tasksToDo] == 16:
							score = Tasks.unlockManifolds()
						elif ToDo[tasksToDo] == 17:
							score = Tasks.starReactor()
						elif ToDo[tasksToDo] == 18:
							score = Tasks.acceptPower()
						elif ToDo[tasksToDo] == 19:
							score = Tasks.medbayScan()
						if score == 1:
							ids = oo.index(tasksToDo)
							del AllTasks[ids][0]
							print(AllTasks)


	keys = pygame.key.get_pressed()
	if ownpos not in DeadPlayers and not in_vent:
		if keys[K_w]:
			b += 3
		if keys[K_a]:
			a += 5
		if keys[K_s]:
			b -= 3
		if keys[K_d]:
			a -= 5

	#weapons
	screen.blit(bg, (0+a,0+b))
	screen.blit(weapons1, (1100+a, 260+b))
	screen.blit(weapons4, (1137+a, 204+b))
	screen.blit(weapons5, (1136+a, 286+b))
	screen.blit(weapons6, (1383+a, 463+b))
	screen.blit(weapons2, (1122+a, 256+b))
	screen.blit(caf_weap, (979+a, 362+b))
	screen.blit(weapons3, (980+a, 193+b))
	screen.blit(weapons7, (1132+a, 242+b))

	#o2
	screen.blit(wep_o2_nav_she, (1209+a, 652+b))
	screen.blit(o21, (875+a, 707+b))
	screen.blit(o22, (1006+a, 802+b))
	screen.blit(o24, (941+a, 830+b))
	screen.blit(o25, (1067+a, 722+b))
	screen.blit(o23, (1090+a, 806+b))
	if c%2 == 0:
		screen.blit(o26, (891+a, 777+b))
	elif c%3 == 0:
		screen.blit(o27, (891+a, 777+b))
	screen.blit(oredirect, (1229+a, 771+b))

	#navigation
	screen.blit(nav2, (1809+a, 798+b))
	screen.blit(nav1, (1808+a, 742+b))
	screen.blit(nav3, (1808+a, 752+b))
	screen.blit(nav4, (2008+a, 835+b))
	screen.blit(nav5, (2017+a, 1040+b))
	screen.blit(nav6, (2023+a, 930+b))
	screen.blit(nav7, (2066+a, 905+b))
	screen.blit(nav8, (2021+a, 812+b))
	screen.blit(nav9, (1946+a, 770+b))
	screen.blit(navredirect, (1866+a, 771+b))
	screen.blit(navelectric, (1747+a, 898+b))

	#admin
	screen.blit(caf_ad_st, (414+a, 958+b))
	screen.blit(admin1, (561+a, 1115+b))
	screen.blit(admin2, (578+a, 1056+b))
	screen.blit(admin3, (582+a, 1064+b))
	screen.blit(admin4, (824+a, 1248+b))
	screen.blit(admin5, (824+a, 1259+b))
	screen.blit(admin6, (999+a, 1259+b))
	screen.blit(admin7, (870+a, 1259+b))
	screen.blit(admin9, (831+a, 1081+b))
	screen.blit(admin10, (998+a, 1081+b))
	screen.blit(admin8, (838+a, 1099+b))
	screen.blit(adminelec, (645+a, 1094+b))
	screen.blit(adminupl, (749+a, 1084+b))
	screen.blit(adminox, (1078+a, 1095+b))

	#cafeteria
	screen.blit(caflev, (913+a, 226+b))
	screen.blit(cafup, (832+a, 159+b))
	screen.blit(cafred, (93+a, 104+b))

	#storage
	screen.blit(sto1, (80+a, 1249+b))
	screen.blit(sto2, (194+a, 1471+b))
	screen.blit(sto4, (279+a, 1700+b))
	screen.blit(sto5, (603+a, 1959+b))
	screen.blit(sto6, (365+a, 1298+b))
	screen.blit(sto7, (637+a, 1485+b))
	
	#communication
	screen.blit(comm1, (663+a, 1739+b))
	screen.blit(comm2, (662+a, 1696+b))
	screen.blit(comm3, (676+a, 1729+b))
	if c%2 == 0:
		screen.blit(comm8, (696+a, 1756+b))
	else:
		screen.blit(comm9, (696+a, 1756+b))
	screen.blit(comm10, (1046+a, 1752+b))
	screen.blit(comm11, (856+a, 1736+b))
	
	#electric
	screen.blit(ele3, (-694+a, 1147+b))
	screen.blit(ele6, (-302+a, 1293+b))
	screen.blit(ele1, (-304+a, 1353+b))
	screen.blit(ele4, ( 35+a, 1187+b))
	screen.blit(ele5, (-294+a, 1395+b))
	screen.blit(ele7, (-118+a, 1187+b))
	screen.blit(ele8, (-227+a, 1183+b))
	screen.blit(ele9, (-280+a, 1180+b))
	screen.blit(ele2, (-314+a, 1159+b))

	#security
	screen.blit(sec1, (-1055+a, 723+b))
	screen.blit(sec2, (-700+a, 729+b))
	screen.blit(sec3, (-620+a, 753+b))
	screen.blit(sec4, (-574+a, 809+b))
	screen.blit(sec5, (-475+a, 793+b))
	screen.blit(sec6, (-664+a, 780+b))
	screen.blit(secele, (-737+a, 945+b))

	#lowerengine
	screen.blit(low1, (-1097+a, 1269+b))
	screen.blit(low3, (-832+a, 1432+b))
	if c%2 == 0:
		screen.blit(low4, (-1088+a, 1394+b))
		screen.blit(low5, (-1078+a, 1607+b))
	else:
		screen.blit(low4, (-1087+a, 1389+b))
		screen.blit(low5, (-1077+a, 1606+b))
	
	screen.blit(low2, (-987+a, 1583+b))
	screen.blit(low6, (-993+a, 1592+b))
	if c%7 == 0:
		screen.blit(low9, (-825+a, 1548+b))
		screen.blit(low11, (-895+a, 1411+b))
	elif c%8 == 0:
		screen.blit(low10, (-863+a, 1449+b))
		screen.blit(low12, (-895+a, 1594+b))
	screen.blit(lowred, (-975+a, 1341+b))
	
	#upper engine
	screen.blit(low13, (-1099+a, 256+b))
	screen.blit(low3, (-838+a, 407+b))
	if c%2 == 0:
		screen.blit(low4, (-1089+a, 348+b))
	else:
		screen.blit(low4, (-1088+a, 349+b))
	screen.blit(low2, (-993+a, 556+b))
	screen.blit(low5, (-1081+a, 563+b))
	screen.blit(low6, (-997+a, 569+b))
	if c%7 == 0:
		screen.blit(low9, (-846+a, 383+b))
		screen.blit(low12, (-884+a, 539+b))
	elif c%8 == 0:
		screen.blit(low10, (-918+a, 535+b))
		screen.blit(low11, (-805+a, 433+b))
	screen.blit(ele8, (-906+a, 291+b))
	
	#medbay
	screen.blit(med1, (-706+a, 362+b))
	screen.blit(med2, (-401+a, 563+b))
	screen.blit(med3, (-142+a, 958+b))
	screen.blit(med4, (-52+a, 871+b))

	#shields
	screen.blit(she1, (1106+a, 1436+b))
	screen.blit(she2, (1103+a, 1429+b))
	screen.blit(she3, (1093+a, 1362+b))
	lig = [(1149, 1454), (1164, 1436), (1177, 1417), (1196, 1404), (1494, 1542), (1494, 1513), (1495, 1483)]
	for i in lig[::-1]:
		screen.blit(she9, (i[0]+a, i[1]+b))
	screen.blit(she5, (1397+a, 1598+b))
	screen.blit(she6, (1131+a, 1436+b))
	screen.blit(she7, (1153+a, 1713+b))
	screen.blit(she10,(1425+a, 1411+b))

	#reactor
	screen.blit(rec2, (-1505+a, 636+b))
	screen.blit(rec3, (-1483+a, 1187+b))

	#cams
	screen.blit(cam_off, (-15+a, 385+b))
	screen.blit(cam_off, (-790+a, 927+b))
	screen.blit(cam_off, (577+a, 1076+b))
	screen.blit(cam_off, (1652+a, 878+b))

	#vent
	near_vent = False
	vent_pos = [(-360, 955), (-530, 1130), (-292, 1241), (-1334, 797), (-766, 349),
				(-1233, 1166), (-765, 1689), (1290, 1770), (1870, 1094), (1269, 279),
				(1869, 833), (833, 543), (743, 1380)]
	vent_rect = [vent_pic.get_rect() for i in vent_pos]
	for i in range(len(vent_rect)):
		vent_rect[i].x, vent_rect[i].y = vent_pos[i][0]+a, vent_pos[i][1]+b
		if vent_rect[i].colliderect(player.rect) and imposter:
			near_vent = True

	if near_vent:
		sabotage.rect.x, sabotage.rect.y = 0, -200
		vent.rect.x, vent.rect.y = 897, 446
	else:
		in_vent = False
		vent.rect.x, vent.rect.y = 0, -200
		sabotage.rect.x, sabotage.rect.y = 897, 446
	
	p = 0
	
	for i in vent_rect:
		if i.colliderect(player.rect):
			print(p)
		p += 1

	for i in vent_pos:
		screen.blit(vent_pic, (i[0]+a, i[1]+b))
	#screen.blit(vent_pic, pygame.mouse.get_pos())

	#collision
	for i in range(len(collision)):
		collision[i].rect.x, collision[i].rect.y = coll_loc[i][0]+a, coll_loc[i][1]+b
	
	coll1 = pygame.surface.Surface([150, 100])
	h = coll1.get_rect()

	hit = pygame.sprite.spritecollide(player, wall_group, False)
	did = 0

	prev = a, b

	#tasks
	screen.blit(weaponselectric, (1491+a, 376+b))
	screen.blit(weaponsupload, (1276+a, 216+b))
	screen.blit(weapons10, (1274+a , 360+b))
	
	s = Sprite(10, 10)
	s.image.fill((255, 255, 255))
	s.rect.center = pygame.mouse.get_pos()
	
	security.rect.x, security.rect.y = 0, -200
	task_group.draw(screen)

	for i in range(len(taskmgr)):
		taskmgr[i].rect.x, taskmgr[i].rect.y = tskpos[i][0]+a, tskpos[i][1]+b

	todo = ()
	for i in range(len(taskmgr)):
		if pygame.sprite.collide_rect(player, taskmgr[i]) == 1:
			todo = 1, i
			tasksToDo = i
			if i == 29:
				security.rect.x, security.rect.y = 789, 444
				if pygame.mouse.get_pressed()[0]:
					cc = a, b
					secCam = 1
			else:
				security.rect.x, security.rect.y = 0, -200
		else:
			tasks.image = tasksoff
	if len(todo) > 0:
		##print(tasksToDo)
		if todo[1] in oo:
			tasks.image = taskson

	for i in collision:
		if pygame.sprite.collide_rect(player, i):
			if keys[pygame.K_w]:
				if abs(player.rect.top - i.rect.bottom) < 17 and hit:
					b = before_pos[1]

			if keys[pygame.K_a]:
				if abs(player.rect.left - i.rect.right) < 17 and hit:
					a = before_pos[0]

			if keys[pygame.K_s]:
				if abs(player.rect.bottom - i.rect.top) < 17 and hit:
					b = before_pos[1]

			if keys[pygame.K_d]:
				if abs(player.rect.right - i.rect.left) < 17 and hit:
					a = before_pos[0]


	players.draw(screen)
	coll = a, b

	#on the player
	a, b = prev

	screen.blit(weapons8, (1133+a, 509+b))
	screen.blit(weaponsgreenscreen, (1304+a, 278+b))
	screen.blit(weapons9, (1394+a, 409+b))
	screen.blit(she8, (1397+a, 1448+b))
	screen.blit(she4, (1129+a, 1635+b))
	screen.blit(comm5, (772+a, 1935+b))
	screen.blit(comm4, (792+a, 1970+b))
	screen.blit(comm6, (671+a, 1849+b))
	screen.blit(comm7, (1041+a, 1846+b))
	screen.blit(sto3, (439+a, 1447+b))
	screen.blit(low3, (-832+a, 1432+b))
	if c%2 == 0:
		screen.blit(low4, (-1088+a, 1394+b))
		screen.blit(low5, (-1078+a, 1607+b))
	else:
		screen.blit(low4, (-1087+a, 1389+b))
		screen.blit(low5, (-1077+a, 1606+b))
	if c%7 == 0:
		screen.blit(low9, (-825+a, 1548+b))
		screen.blit(low11, (-895+a, 1411+b))
	elif c%8 == 0:
		screen.blit(low10, (-863+a, 1449+b))
		screen.blit(low12, (-895+a, 1594+b))
	if c%2 == 0:
		screen.blit(low4, (-1089+a, 348+b))
	else:
		screen.blit(low4, (-1088+a, 349+b))
	screen.blit(rec1, (-1466+a, 824+b))
	screen.blit(low5, (-1074+a, 563+b))

	a, b = coll

	#buttons
	button_group.draw(screen)

	if secCam == 1:

		screen.blit(secC1, (-200, 0))
		screen.blit(secC2, (809, 245))
		screen.blit(secC3, (82, 230))
		#1365 -720, 785 -99, 5 -825, -1025 -660
		if 809 < pygame.mouse.get_pos()[0] < 809+60 and 245 < pygame.mouse.get_pos()[1] < 245+60 and pygame.mouse.get_pressed()[0]:
			secCNum += 0.5
			if secCNum > 5:
				secCNum = 1
			#print(int(secCNum))
		if 82 < pygame.mouse.get_pos()[0] < 82+60 and 230 < pygame.mouse.get_pos()[1] < 230+60 and pygame.mouse.get_pressed()[0]:
			secCNum -= 0.5
			if secCNum < 1:
				secCNum = 4.5
			#print(int(secCNum))
		if int(secCNum) == 1:
			a, b = (1365, -720)
		elif int(secCNum) == 2:
			a, b = (785, -99)
		elif int(secCNum) == 3:
			a, b = 5, -825
		else:
			a, b = -1025, -660
		close = pygame.image.load("models/buttons/close.png")
		screen.blit(close, (100, 25))
		if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
			secCam = 0
			a, b = cc
			cc = None
		#screen.blit(secC2, pygame.mouse.get_pos())
	
	if secCam != 1:

		if imposter:
			text0 = font.render('Fake Tasks', True, (255, 0, 0))
			textrect0 = text0.get_rect()
			screen.blit(text0, (10, 70-font_size))
		
		text1 = font.render(Text1 + f'({len(AllTasks[0])})', True, (255, 255, 255))
		if len(AllTasks[0]) == 0:
			text1 = font.render(Text1, True, (0, 255, 0))

		text2 = font.render(Text2 + f'({len(AllTasks[1])})', True, (255, 255, 255))
		if len(AllTasks[1]) == 0:
			text2 = font.render(Text2, True, (0, 255, 0))

		text3 = font.render(Text3+f'({len(AllTasks[2])})', True, (255, 255, 255))
		if len(AllTasks[2]) == 0:
			text3 = font.render(Text3, True, (0, 255, 0))

		text4 = font.render(Text4+f'({len(AllTasks[3])})', True, (255, 255, 255))
		if len(AllTasks[3]) == 0:
			text4 = font.render(Text4, True, (0, 255, 0))

		text5 = font.render(Text5+f'({len(AllTasks[4])})', True, (255, 255, 255))
		if len(AllTasks[4]) == 0:
			text5 = font.render(Text5, True, (0, 255, 0))

		text6 = font.render(Text6+f'({len(AllTasks[5])})', True, (255, 255, 255))
		if len(AllTasks[5]) == 0:
			text6 = font.render(Text6, True, (0, 255, 0))

		
		textRect1 = text1.get_rect()
		textRect2 = text2.get_rect()
		textRect3 = text3.get_rect()
		textRect4 = text4.get_rect()
		textRect5 = text5.get_rect()
		textRect6 = text6.get_rect()

		screen.blit(text1, (10, 70))
		screen.blit(text2, (10, 70+font_size))
		screen.blit(text3, (10, 70+font_size*2))
		screen.blit(text4, (10, 70+font_size*3))
		screen.blit(text5, (10, 70+font_size*4))
		screen.blit(text6, (10, 70+font_size*5))

		if 929 < pygame.mouse.get_pos()[0] < 1000 and 74 < pygame.mouse.get_pos()[1] < 154 and pygame.mouse.get_pressed()[0]:
			show_map = True
		
		if show_map:
			if imposter:
				map1 = pygame.image.load('models/maps/2.png')

			screen.blit(map1, (0, 0))

			screen.blit(pygame.image.load("models/maps/4.png"), ((-a/3657)*1000 + 500, (-b/2058)*550 + 60))

			ts_im = pygame.image.load("models/maps/3.png")
			ts_imx = pygame.image.load("models/maps/3.png").get_size()[0]//2
			ts_imy = pygame.image.load("models/maps/3.png").get_size()[1]//2
			map_task_pos = {5:(411, 24), 10:(882, 231), 17:(683, 471), 42:(485, 348), 37:(565, 290), 25:(372, 290), 31:(191, 249),
							24:(339, 315), 36:(169, 74), 34:(118, 356), 2:(806, 102), 15:(790, 377), 11:(907, 204), 6:(725, 201), 30:(267, 217),
							38:(609, 290), 4:(783, 82), 1:(740, 55), 12:(928, 201), 19:(628, 470), 23:(314, 316),
							21:(466, 490), 35:(108, 178), 32:(124, 456), 49:(98, 175), 33:(104, 457), 28:(399, 239), 27:(366, 263),
							40:(666, 345), 8:(659, 215), 26:(408, 316), 0:(754, 123), 14:(975, 255), 13:(954, 214), 16:(720, 490), 45:(20, 194), 43:(28, 282),
							3:(645, 59), 9:(644, 235), 20:(533, 544)}
			for i in oo:
				if i in map_task_pos:
					screen.blit(ts_im, (map_task_pos[i][0]-ts_imx, map_task_pos[i][1]-ts_imy))
			close = pygame.image.load("models/buttons/close.png")
			screen.blit(close, (100, 25))
			if 117 < pygame.mouse.get_pos()[0] < 155 and 41 < pygame.mouse.get_pos()[1] < 78 and pygame.mouse.get_pressed()[0]:
				show_map = False

	#Multiplayer
	Player_Pos = []

	server_info = connect.send((-a, -b, player.move, player.flip, My_color, AmIDEAD, imposter, killed_player_index, DeadPlayers, in_vent))


	try:
		server_info = eval(server_info)
		#print(server_info)
		ownpos = eval(server_info[str(f"b'{connect.name}'")])[-2]
		#print(ownpos)
		
		for i in server_info:
			#print(server_info[i])
			server_info[i] = eval(server_info[i])
			if server_info[i][6]:
				imposterName = i
		#print(imposterName)
		
		for i in server_info:
			if i != str(f"b'{connect.name}'"):

				if not server_info[i][5]:

					if not server_info[i][9]:

						font1 = pygame.font.Font('freesansbold.ttf', 10)
						Tet = i[2:-1]
						tet = font.render(Tet, True, (255, 255, 255))
						tetRect = tet.get_rect()
						screen.blit(tet, (int(server_info[i][0])+490+a, int(server_info[i][1])+265+b))

						player2 = pygame.transform.flip(pygame.image.load(f"images/Sprites/Walk/walkcolor00{int(server_info[i][2])}.png"), not server_info[i][3], False)
						
						if int(server_info[i][2]) == 1:
							player2 = pygame.image.load('idle.png')
					
				else:
					player2 = pygame.image.load("images/Sprites/Death/Dead0033.png")

				if not server_info[i][9]::
					player2 = pygame.transform.scale(player2, (78-25,103-30))				
					player2 = colorchanger(player2, server_info[i][4])
				
					screen.blit(player2, (int(server_info[i][0])+500+a, int(server_info[i][1])+275+b))

			if server_info[i][7] != None:
				dead.append((int(server_info[i][0])+530+a, int(server_info[i][1])+305+b))
				DEADPOS.append((int(server_info[i][0])+530+a, int(server_info[i][1])+305+b))
				#print((int(server_info[i][0])+530+a, int(server_info[i][1])+305+b))
				if server_info[i][7] == ownpos and not AmIDEAD:
					#print('YOU Actually died')
					DeadPlayers.append(ownpos)
					AmIDEAD = True

			if not server_info[i][5]:
				Player_Pos.append((int(server_info[i][0])+530+a, int(server_info[i][1])+305+b))

			'''else:
				if server_info[i][5][server_info[i][7]] == ownpos:
					print('dead')'''

	except Exception as e:
		print(f'{e} Happened')

	#Player Pos
	other_players_group = pygame.sprite.Group()
	kill_but = 0
	for i in range(len(Player_Pos)):
		if i != ownpos:
			pp = Player_Pos[i]
			Player_Pos[i] = Sprite(100, 100)
			Player_Pos[i].rect.center = pp[0], pp[1]
			other_players_group.add(Player_Pos[i])

	canKill = False
	killed_player_index = None

	for i in range(len(Player_Pos)):
		if i != ownpos:
			if pygame.sprite.collide_rect(player, Player_Pos[i]):
				canKill = True
				if pygame.sprite.collide_rect(s, kill) and pygame.mouse.get_pressed()[0]:
					killed = Player_Pos[i].rect.x, Player_Pos[i].rect.y
					killed_player_index = i
					#del Player_Pos[i]
					break
	if canKill:
		kill.image = killon
	else:
		kill.image = killoff

	#dead
	dead_grp = pygame.sprite.Group()
	reportbut = 0
	for i in range(len(dead)):
		try:
			ded = dead[i][0], dead[i][1]
			#print(ded)
			dead[i] = Sprite(100, 100)
			dead[i].rect.center = ded[0], ded[1]
			#print(ded[0]+a, ded[1]+b)
			dead_grp.add(dead[i])
		except:
			dead[i].rect.x, dead[i].rect.y = DEADPOS[i][0]+a, DEADPOS[i][1]+b
			dead_grp.add(dead[i])
			#print(dead[i].rect.center)

	dead_grp.draw(screen)
	for i in dead:
		if pygame.sprite.collide_rect(player, i) == 1:
			reportbut = 1
	if reportbut == 1:
		report.image = reporton
	else:
		report.image = reportoff

	#wall_group.draw(screen)
	players.update(secCam, My_color, in_vent)
	s.update()
	pygame.display.update()
	clock.tick(fps)