import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 50
size =[1366, 768]
screen = pygame.display.set_mode(size)

a = 0
b = 0
c = 0

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

while True:
	c += 1
	screen.fill((255, 255, 255))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(pygame.mouse.get_pos()[0]-a, pygame.mouse.get_pos()[1]-b)

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
	screen.blit(weapons8, (1133+a, 509+b))
	screen.blit(weapons9, (1394+a, 409+b))
	screen.blit(weapons10, (1274+a , 360+b))
	screen.blit(weaponselectric, (1491+a, 376+b))
	screen.blit(weaponsupload, (1276+a, 216+b))
	screen.blit(weaponsgreenscreen, (1304+a, 278+b))

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
	screen.blit(navcamon, (1636+a, 869+b))
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
	screen.blit(admincamoff, (588+a, 1070+b))

	#cafeteria
	screen.blit(caflev, (913+a, 226+b))
	screen.blit(cafup, (832+a, 159+b))
	screen.blit(cafred, (93+a, 104+b))

	#storage
	screen.blit(sto1, (80+a, 1249+b))
	screen.blit(sto2, (194+a, 1471+b))
	screen.blit(sto3, (439+a, 1447+b))
	screen.blit(sto4, (279+a, 1700+b))
	screen.blit(sto5, (603+a, 1959+b))
	screen.blit(sto6, (365+a, 1298+b))
	screen.blit(sto7, (637+a, 1485+b))
	
	#communication
	screen.blit(comm1, (663+a, 1739+b))
	screen.blit(comm2, (662+a, 1696+b))
	screen.blit(comm3, (676+a, 1729+b))
	screen.blit(comm5, (772+a, 1935+b))
	screen.blit(comm4, (792+a, 1970+b))
	screen.blit(comm6, (671+a, 1849+b))
	screen.blit(comm7, (1041+a, 1846+b))
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
	screen.blit(ele4, (35+a, 1187+b))
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
	#screen.blit(med4, pygame.mouse.get_pos())

	keys = pygame.key.get_pressed()
	if keys[K_w]:
		b += 10
	if keys[K_a]:
		a += 10
	if keys[K_s]:
		b -= 10
	if keys[K_d]:
		a -= 10

	pygame.display.update()
	clock.tick(fps)
