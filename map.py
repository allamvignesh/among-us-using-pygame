import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 50
size =[1000, 550]
screen = pygame.display.set_mode(size)

cam_on = pygame.image.load("models/map parts/cam-on.png")
cam_off = pygame.image.load("models/map parts/cam-off.png")
redirect = pygame.image.load("models/map parts/redirect.png")
electric = pygame.image.load("models/map parts/electric.png")
upload = pygame.image.load("models/map parts/weapons/upload.png")

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
navcamon = cam_on
navcamoff = cam_off
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
admincamon = cam_on
admincamoff = cam_off

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

#security
sec1 = pygame.image.load("models/map parts/security/sec-1.png")
sec2 = pygame.image.load("models/map parts/security/sec-2.png")
sec3 = pygame.image.load("models/map parts/security/sec-3.png")
sec4 = pygame.image.load("models/map parts/security/sec-4.png")
sec5 = pygame.image.load("models/map parts/security/sec-5.png")
sec6 = pygame.image.load("models/map parts/security/sec-6.png")

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

class Map():
	def __init__(self):
		self.a = 0
		self.b = 0
		self.c = 0

	def update(self):
		self.c += 1
		screen.fill(0)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		#weapons
		screen.blit(bg, (0+self.a, 0+self.b))
		screen.blit(weapons1, (1100+self.a, 260+self.b))
		screen.blit(weapons4, (1137+self.a, 204+self.b))
		screen.blit(weapons5, (1136+self.a, 286+self.b))
		screen.blit(weapons6, (1383+self.a, 463+self.b))
		screen.blit(weapons2, (1122+self.a, 256+self.b))
		screen.blit(caf_weap, (979+self.a, 362+self.b))
		screen.blit(weapons3, (980+self.a, 193+self.b))
		screen.blit(weapons7, (1132+self.a, 242+self.b))
		screen.blit(weapons8, (1133+self.a, 509+self.b))
		screen.blit(weapons9, (1394+self.a, 409+self.b))
		screen.blit(weapons10, (1274+self.a , 360+self.b))
		screen.blit(weaponselectric, (1491+self.a, 376+self.b))
		screen.blit(weaponsupload, (1276+self.a, 216+self.b))
		screen.blit(weaponsgreenscreen, (1304+self.a, 278+self.b))

		#o2
		screen.blit(wep_o2_nav_she, (1209+self.a, 652+self.b))
		screen.blit(o21, (875+self.a, 707+self.b))
		screen.blit(o22, (1006+self.a, 802+self.b))
		screen.blit(o24, (941+self.a, 830+self.b))
		screen.blit(o25, (1067+self.a, 722+self.b))
		screen.blit(o23, (1090+self.a, 806+self.b))
		if self.c%2 == 0:
			screen.blit(o26, (891+self.a, 777+self.b))
		elif self.c%3 == 0:
			screen.blit(o27, (891+self.a, 777+self.b))
		screen.blit(oredirect, (1229+self.a, 771+self.b))

		#navigation
		screen.blit(nav2, (1809+self.a, 798+self.b))
		screen.blit(nav1, (1808+self.a, 742+self.b))
		screen.blit(nav3, (1808+self.a, 752+self.b))
		screen.blit(nav4, (2008+self.a, 835+self.b))
		screen.blit(nav5, (2017+self.a, 1040+self.b))
		screen.blit(nav6, (2023+self.a, 930+self.b))
		screen.blit(nav7, (2066+self.a, 905+self.b))
		screen.blit(nav8, (2021+self.a, 812+self.b))
		screen.blit(nav9, (1946+self.a, 770+self.b))
		screen.blit(navcamon, (1636+self.a, 869+self.b))
		screen.blit(navredirect, (1866+self.a, 771+self.b))
		screen.blit(navelectric, (1747+self.a, 898+self.b))

		#admin
		screen.blit(caf_ad_st, (414+self.a, 958+self.b))
		screen.blit(admin1, (561+self.a, 1115+self.b))
		screen.blit(admin2, (578+self.a, 1056+self.b))
		screen.blit(admin3, (582+self.a, 1064+self.b))
		screen.blit(admin4, (824+self.a, 1248+self.b))
		screen.blit(admin5, (824+self.a, 1259+self.b))
		screen.blit(admin6, (999+self.a, 1259+self.b))
		screen.blit(admin7, (870+self.a, 1259+self.b))
		screen.blit(admin9, (831+self.a, 1081+self.b))
		screen.blit(admin10, (998+self.a, 1081+self.b))
		screen.blit(admin8, (838+self.a, 1099+self.b))
		screen.blit(adminelec, (645+self.a, 1094+self.b))
		screen.blit(adminupl, (749+self.a, 1084+self.b))
		screen.blit(adminox, (1078+self.a, 1095+self.b))
		screen.blit(admincamoff, (588+self.a, 1070+self.b))

		#cafeteria
		screen.blit(caflev, (913+self.a, 226+self.b))
		screen.blit(cafup, (832+self.a, 159+self.b))
		screen.blit(cafred, (93+self.a, 104+self.b))

		#storage
		screen.blit(sto1, (80+self.a, 1249+self.b))
		screen.blit(sto2, (194+self.a, 1471+self.b))
		screen.blit(sto3, (439+self.a, 1447+self.b))
		screen.blit(sto4, (279+self.a, 1700+self.b))
		screen.blit(sto5, (603+self.a, 1959+self.b))
		screen.blit(sto6, (365+self.a, 1298+self.b))
		screen.blit(sto7, (637+self.a, 1485+self.b))
		
		#communication
		screen.blit(comm1, (663+self.a, 1739+self.b))
		screen.blit(comm2, (662+self.a, 1696+self.b))
		screen.blit(comm3, (676+self.a, 1729+self.b))
		screen.blit(comm5, (772+self.a, 1935+self.b))
		screen.blit(comm4, (792+self.a, 1970+self.b))
		screen.blit(comm6, (671+self.a, 1849+self.b))
		screen.blit(comm7, (1041+self.a, 1846+self.b))
		if self.c%2 == 0:
			screen.blit(comm8, (696+self.a, 1756+self.b))
		else:
			screen.blit(comm9, (696+self.a, 1756+self.b))
		screen.blit(comm10, (1046+self.a, 1752+self.b))
		screen.blit(comm11, (856+self.a, 1736+self.b))
		
		#electric
		screen.blit(ele3, (-694+self.a, 1147+self.b))
		screen.blit(ele6, (-302+self.a, 1293+self.b))
		screen.blit(ele1, (-304+self.a, 1353+self.b))
		screen.blit(ele4, (35+self.a, 1187+self.b))
		screen.blit(ele5, (-294+self.a, 1395+self.b))
		screen.blit(ele7, (-118+self.a, 1187+self.b))
		screen.blit(ele8, (-227+self.a, 1183+self.b))
		screen.blit(ele9, (-280+self.a, 1180+self.b))
		screen.blit(ele2, (-314+self.a, 1159+self.b))

		#security
		screen.blit(sec1, (-1055+self.a, 723+self.b))
		screen.blit(sec2, (-700+self.a, 729+self.b))
		screen.blit(sec3, (-620+self.a, 753+self.b))
		screen.blit(sec4, (-574+self.a, 809+self.b))
		screen.blit(sec5, (-475+self.a, 793+self.b))
		screen.blit(sec6, (-664+self.a, 780+self.b))

		#lowerengine
		screen.blit(low1, (-1097+self.a, 1269+self.b))
		screen.blit(low3, (-832+self.a, 1432+self.b))
		if self.c%2 == 0:
			screen.blit(low4, (-1088+self.a, 1394+self.b))
			screen.blit(low5, (-1078+self.a, 1607+self.b))
		else:
			screen.blit(low4, (-1087+self.a, 1389+self.b))
			screen.blit(low5, (-1077+self.a, 1606+self.b))
		
		screen.blit(low2, (-987+self.a, 1583+self.b))
		screen.blit(low6, (-993+self.a, 1592+self.b))
		if self.c%7 == 0:
			screen.blit(low9, (-825+self.a, 1548+self.b))
			screen.blit(low11, (-895+self.a, 1411+self.b))
		elif self.c%8 == 0:
			screen.blit(low10, (-863+self.a, 1449+self.b))
			screen.blit(low12, (-895+self.a, 1594+self.b))
		
		#upper engine
		screen.blit(low13, (-1099+self.a, 256+self.b))
		screen.blit(low3, (-838+self.a, 407+self.b))
		if self.c%2 == 0:
			screen.blit(low4, (-1089+self.a, 348+self.b))
		else:
			screen.blit(low4, (-1088+self.a, 349+self.b))
		screen.blit(low2, (-993+self.a, 556+self.b))
		screen.blit(low5, (-1081+self.a, 563+self.b))
		screen.blit(low6, (-997+self.a, 569+self.b))
		if self.c%7 == 0:
			screen.blit(low9, (-846+self.a, 383+self.b))
			screen.blit(low12, (-884+self.a, 539+self.b))
		elif self.c%8 == 0:
			screen.blit(low10, (-918+self.a, 535+self.b))
			screen.blit(low11, (-805+self.a, 433+self.b))
		screen.blit(ele8, (-906+self.a, 291+self.b))
		
		#medbay
		screen.blit(med1, (-706+self.a, 362+self.b))
		screen.blit(med2, (-401+self.a, 563+self.b))
		screen.blit(med3, (-142+self.a, 958+self.b))
		screen.blit(med4, (-52+self.a, 871+self.b))
		#screen.blit(med4, pygame.mouse.get_pos())

		#shields
		screen.blit(she1, (1106+self.a, 1436+self.b))
		screen.blit(she2, (1103+self.a, 1429+self.b))
		screen.blit(she3, (1093+self.a, 1362+self.b))
		lig = [(1149, 1454), (1164, 1436), (1177, 1417), (1196, 1404), (1494, 1542), (1494, 1513), (1495, 1483)]
		for i in lig[::-1]:
			screen.blit(she9, (i[0]+self.a, i[1]+self.b))
		screen.blit(she5, (1397+self.a, 1598+self.b))
		screen.blit(she6, (1131+self.a, 1436+self.b))
		screen.blit(she7, (1153+self.a, 1713+self.b))
		screen.blit(she10,(1425+self.a, 1411+self.b))

		#reactor
		screen.blit(rec2, (-1505+self.a, 636+self.b))
		screen.blit(rec3, (-1483+self.a, 1187+self.b))

		keys = pygame.key.get_pressed()
		if keys[K_w]:
			self.b += 3
		if keys[K_a]:
			self.a += 5
		if keys[K_s]:
			self.b -= 3
		if keys[K_d]:
			self.a -= 5

		pygame.display.update()
		clock.tick(fps)

Map = Map()
while True:
	
	Map.update()

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()