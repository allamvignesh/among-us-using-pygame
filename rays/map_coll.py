import pygame
from pygame.locals import *
from walk_anim import Player
import math

pygame.init()

clock = pygame.time.Clock()
fps = 40
size =[1000, 550]
screen = pygame.display.set_mode(size)

a = 0
b = 0
c = 0
totTasks = 0

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

coll_loc = [(193, 1, 530, 10), (720, 2, 10, 10), (734, 20, 10, 10), (762, 47, 10, 10), (789, 75, 10, 10), (816, 98, 10, 10),
			(834, 119, 10, 10), (856, 142, 10, 10), (876, 161, 10, 10), (895, 181, 10, 10), (920, 203, 10, 10), (947, 229, 10, 10),
			(959, 249, 10, 130), (959, 369, 230, 10), (1189, 339, 10, 10), (1220, 200, 10, 130), (1220, 200, 130, 10),
			(1358, 217, 10, 10), (1376, 236, 10, 10), (1404, 260, 10, 10), (1427, 287, 10, 10), (1450, 309, 10, 10), (1472, 329, 10, 10), (1494, 354, 10, 10), (1516, 376, 10, 10),
			(1432, 435, 100, 10), (1401, 509, 10, 240), (1403, 741, 200, 10), (1603, 741, 10, 120), (1603, 861, 240, 10),
			(1833, 740, 10, 130), (1833, 740, 200, 10), (2011, 828, 10, 10), (2049, 789, 10, 10), (2056, 848, 30, 10), (2077, 850, 10, 200), (2029, 935, 50, 10), (2029, 950, 40, 10),
			(2003, 1044, 80, 10), (2003, 1044, 10, 100), (1841, 1142, 150, 10), (1837, 1028, 10, 130), (1606, 1027, 230, 10),
			(1606, 1027, 10, 150), (1407, 1170, 200, 10), (1407, 1170, 10, 220), (1408, 1382, 130, 10), (1521, 1383, 10, 100),
			(1413, 1469, 120, 10), (1413, 1469, 10, 80), (1438, 1549, 10, 80), (1408, 1689, 10, 80),
			(1341, 1827, 10, 10), (1363, 1804, 10, 10), (1384, 1782, 10, 10), (1148, 1817, 200, 10),
			(1145, 1728, 130, 10), (1145, 1728, 10, 80), (1251, 1709, 10, 10), (1221, 1685, 10, 10), (1041, 1658, 170, 10), (1041, 1658, 10, 70),
			(1091, 1720, 10, 180), (1047, 1893, 40, 10), (1047, 1893, 10, 100), (714, 2000, 340, 10), (712, 1893, 10, 100),
			(672,1893, 40, 10), (665, 1743, 10, 150), (665, 1743, 240, 10), (903, 1657, 10, 80), (626, 1658, 280, 10),
			(626, 1658, 10, 400), (290, 2044, 350, 10), (960, 536, 280, 10), (1265, 550, 10, 200), (1000, 744, 260, 10),
			(1014, 803, 20, 10), (957, 833, 10, 30), (924, 886, 10, 80), (924, 964, 280, 10), (1195, 916, 10, 50),
			(1195, 916, 280, 10), (1466, 917, 10, 100), (1263, 1017, 200, 10), (1263, 1017, 10, 470,), (626, 1494, 600, 10),
			(626, 1268, 10, 230), (555, 1265, 80, 10), (553, 1226, 160, 10), (704, 1225, 10, 200),
			(707, 1433, 350, 10), (1094, 1402, 10, 10), (1132, 1059, 10, 350), (1063, 1056, 50, 10),
			(811, 1108, 250, 10), (717, 1059, 80, 10), (554, 1093, 150, 10), (553, 942, 10, 150),
			(827, 1250, 190, 80), (554, 942, 200, 10), (780, 906, 10, 10), (818, 867, 10, 10), (849, 835, 10, 10), (889, 799, 10, 10), (921, 762, 10, 10),
			(962, 537, 10, 200), (1300, 380, 50, 50), (605, 216, 150, 100), (188, 222, 150, 100), (398, 444, 150, 100), (184, 656, 150, 100), (605, 656, 150, 100),
			(109, 1848, 10, 10), (113, 1870, 10, 10), (126, 1888, 10, 10), (135, 1901, 10, 10), (153, 1917, 10, 10), (168, 1929, 10, 10), (183, 1948, 10, 10), (202, 1966, 10, 10), (219, 1983, 10, 10), (236, 2002, 10, 10), (254, 2019, 10, 10), (271, 2036, 10, 10),
			(-541, 1845, 600, 10), (-543, 1612, 10, 240), (-695, 1615, 160, 10), (-695, 1615, 10, 150),
			(-983, 1750, 300, 10), (-1094, 1671, 10, 10), (-1078, 1685, 10, 10), (-1065, 1695, 10, 10), (-1049, 1709, 10, 10), (-1036, 1719, 10, 10), (-1023, 1728, 10, 10), (-1012, 1739, 10, 10), (-1001, 1747, 10, 10),
			(-1096, 1308, 10, 380), (-1096, 1598, 320, 10), (-784, 1457, 10, 150), (-1096, 1457, 320, 10),
			(-1096, 1308, 150, 10), (-943, 1079, 10, 230), (-803, 1079, 10, 230), (-802, 1308, 100, 10),
			(-698, 1309, 10, 150), (-699, 1447, 280, 10), (-404, 1446, 10, 240), (-406, 1679, 90, 10), (-322, 1151, 10, 540),
			(-322, 1163, 440, 10), (111, 1164, 10, 100), (101, 1275, 10, 10), (81, 1295, 10, 10), (60, 1314, 10, 10), (39, 1334, 10, 10), (24, 1352, 10, 10),
			(9, 1369, 10, 170), (-4, 1546, 10, 10), (-21, 1562, 10, 10), (-36, 1576, 10, 10), (-53, 1594, 10, 10), (-66, 1606, 10, 10), (-73, 1615, 10, 10),
			(-190, 1618, 100, 10), (-190, 1618, 10, 70), (-191, 1679, 300, 10), (112, 1455, 10, 200),
			(317, 1270, 100, 10), (303, 1270, 10, 30), (285, 1314, 10, 10), (262, 1330, 10, 10), (230, 1355, 10, 10), (211, 1368, 10, 10), (191, 1391, 10, 10), (167, 1403, 10, 10), (152, 1422, 10, 10), (131, 1435, 10, 10), (115, 1441, 10, 10),
			(270, 1514, 238, 238), (201, 1590, 50, 60), (417, 944, 10, 330), (233, 942, 190, 10), (18, 737, 10, 10), (37, 754, 10, 10), (53, 774, 10, 10), (74, 791, 10, 10), (91, 809, 10, 10), (109, 829, 10, 10), (124, 848, 10, 10), (150, 871, 10, 10), (174, 895, 10, 10), (194, 915, 10, 10), (213, 932, 10, 10),
			(19, 536, 10, 200), (-156, 535, 180, 10), (-156, 535, 10, 75), (-156, 610, 130, 10), (-38, 607, 10, 200),
			(-35, 823, 10, 10), (-19, 845, 10, 10), (-5, 855, 10, 10), (8, 869, 10, 10), (-10, 888, 10, 10), (3, 908, 10, 10), (17, 922, 10, 10), (31, 937, 10, 10), (54, 927, 10, 10), (63, 925, 10, 10), (77, 934, 10, 10), (89, 946, 10, 10), (99, 956, 10, 10), (107, 963, 10, 10),
			(-129, 697, 100, 20), (-386, 697, 100, 20), (-387, 808, 100, 20), (-132, 811, 100, 20), (109, 966, 10, 100),
			(-321, 1070, 440, 10), (-398, 994, 10, 10), (-384, 1007, 10, 10), (-374, 1022, 10, 10), (-361, 1038, 10, 10), (-350, 1052, 10, 10), (-338, 1066, 10, 10),
			(-397, 604, 10, 380), (-397, 604, 100, 10), (-294, 535, 10, 80), (-695, 535, 410, 10), (-695, 535, 10, 180), (-804, 701, 120, 10), (-804, 701, 10, 216),
			(-806, 908, 130, 10), (-674, 815, 10, 100), (-665, 804, 10, 10), (-652, 791, 10, 10), (-640, 780, 10, 10), (-627, 767, 10, 10), (-617, 759, 100, 10),
			(-486, 762, 10, 10), (-483, 772, 10, 10), (-471, 786, 10, 10), (-461, 802, 10, 10), (-445, 817, 10, 10), (-441, 830, 10, 350), (-530, 971, 100, 100),
			(-676, 1183, 240, 10), (-677, 1080, 10, 100), (-804, 1078, 130, 10), (-944, 698, 10, 220), (-1095, 698, 160, 10),
			(-1095, 577, 316, 10), (-1095, 577, 10, 120), (-789, 408, 10, 170), (-1089, 408, 300, 10), (-1049, 306, 10, 100),
			(-1037, 294, 10, 10), (-1019, 281, 10, 10), (-1005, 272, 10, 10), (-985, 258, 300, 10), (-698, 257, 10, 100),
			(-695, 364, 720, 10), (20, 172, 10, 200), (31, 159, 10, 10), (52, 140, 10, 10), (62, 127, 10, 10), (75, 116, 10, 10), (89, 100, 10, 10), (104, 82, 10, 10), (124, 65, 10, 10), (142, 45, 10, 10), (160, 29, 10, 10), (176, 16, 10, 10),
			(-311, 1377, 210, 20), (-595, 800, 60, 20), (-1096, 1602, 100, 60), (-1094, 581, 100, 40), (-1057, 906, 10, 10), (-1032, 909, 10, 10), (-1007, 908, 10, 10), (-981, 908, 10, 10), (-949, 908, 10, 10),
			(-1330, 626, 10, 10), (-1285, 626, 10, 10), (-1240, 626, 10, 10), (-1210, 626, 10, 10), (-1210, 650, 10, 10), (-1210, 680, 10, 10), (-1210, 710, 10, 10), (-1210, 740, 10, 10), (-1210, 764, 10, 10), (-1175, 764, 10, 10), (-1140, 764, 10, 10), (-1115, 764, 10, 10), (-1090, 764, 10, 10), (-1060, 764, 10, 10), (-1060, 776, 10, 10), (-1060, 797, 10, 10), (-1060, 818, 10, 10), (-1060, 818, 10, 10), (-1060, 853, 10, 10), (-1057, 878, 10, 10),
			(-1340, 648, 10, 10), (-1349, 663, 10, 10), (-1355, 687, 10, 10), (-1372, 703, 10, 10), (-1381, 721, 10, 10), (-1400, 735, 10, 10), (-1417, 765, 10, 10), (-1425, 789, 10, 10), (-1426, 825, 10, 10),
			(-1425, 857, 10, 10), (-1419, 881, 10, 10), (-1385, 885, 10, 10), (-1362, 885, 10, 10), (-1339, 888, 10, 10), (-1339, 920, 10, 10), (-1341, 952, 10, 10), (-1329, 970, 10, 10), (-1326, 992, 10, 10), (-1328, 1016, 10, 10), (-1310, 1026, 10, 10), (-1288, 1038, 10, 10), (-1297, 1059, 10, 10), (-1323, 1060, 10, 10), (-1343, 1063, 10, 10),
			(-1346, 1072, 10, 10), (-1345, 1103, 10, 10), (-1364, 1078, 10, 10), (-1388, 1085, 10, 10), (-1416, 1085, 10, 10), (-1421, 1128, 10, 10), (-1423, 1156, 10, 10), (-1423, 1183, 10, 10), (-1422, 1217, 10, 10), (-1422, 1250, 10, 10), (-1423, 1283, 10, 10),
			(-1411, 1309, 10, 10), (-1383, 1329, 10, 10), (-1362, 1343, 10, 10), (-1338, 1358, 10, 10), (-1314, 1375, 10, 10), (-1287, 1375, 10, 10), (-1245, 1375, 10, 10), (-1217, 1377, 10, 10), (-1204, 1347, 10, 10), (-1205, 1315, 10, 10), (-1205, 1279, 10, 10), (-1205, 1242, 10, 10), (-1205, 1216, 10, 10), (-1171, 1216, 10, 10),
			(-1141, 1215, 10, 10), (-1104, 1213, 10, 10), (-1071, 1216, 10, 10), (-1058, 1191, 10, 10), (-1059, 1160, 10, 10), (-1058, 1132, 10, 10), (-1058, 1108, 10, 10), (-1059, 1094, 10, 10), (-1038, 1093, 10, 10), (-1035, 1078, 10, 10), (-1012, 1078, 10, 10), (-989, 1077, 10, 10), (-962, 1077, 10, 10), (-942, 1076, 10, 10),
			]

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

mousebut = Sprite()

mousebut.rect.x, mousebut.rect.y = 0, 0

tasks.rect.x, tasks.rect.y = 897, 446
report.rect.x, report.rect.y = 892, 333
sabotage.rect.x, sabotage.rect.y = 897, 446
vent.rect.x, vent.rect.y = 787, 448
kill.rect.x, kill.rect.y = 789, 444

button_group = pygame.sprite.Group()
button_group.add(tasks)
button_group.add(report)
button_group.add(sabotage)
button_group.add(vent)
button_group.add(kill)

but = [tasks, report, sabotage, vent, kill]
mous_grp = pygame.sprite.Group()
mous_grp.add(mousebut)

imposter = False

if imposter:
	tasks.rect.x, tasks.rect.y = (0, -200)
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
			(-1316, 1020, 10, 10), (-1156, 799, 10, 10), (-1366, 710, 10, 10), (-1273, 648, 10, 10), (-1278, 1344, 10, 10), (340, 402, 220, 150)]


taskmgr = [Sprite(k+40, l+40) for i,j,k,l in tskpos]

task_group = pygame.sprite.Group()

for i in range(len(taskmgr)):
	task_group.add(taskmgr[i])

dead_bodys = [(100, 100, 100, 100)]
f = []

def Draw_Map():
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
	else:
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

while True:
	c += 1
	wall_group.draw(screen)
	mousebut.rect.x, mousebut.rect.y = pygame.mouse.get_pos()
	mous_grp.draw(screen)

	screen.fill((0, 0, 0))

	before_pos = a, b

	ve_nt = [[(-240, -1071), (-350, -249), (-800, -771)], []]

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			print(f)
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			#print(a, b)
			print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
			#print(pygame.mouse.get_pos()[0]-a, pygame.mouse.get_pos()[1]-b)
			#f.append((pygame.mouse.get_pos()[0]-a, pygame.mouse.get_pos()[1]-b, 10, 10))

			for i in range(len(but)):
				smashhit = pygame.sprite.collide_rect(mousebut, but[i])
				if smashhit and pygame.mouse.get_pressed()[0]:
					print(i)
	keys = pygame.key.get_pressed()
	if keys[K_w]:
		b += 3
	if keys[K_a]:
		a += 5
	if keys[K_s]:
		b -= 3
	if keys[K_d]:
		a -= 5

	Draw_Map()

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
	s = pygame.surface.Surface([10, 10])
	screen.blit(s, pygame.mouse.get_pos())
	task_group.draw(screen)

	for i in range(len(taskmgr)):
		taskmgr[i].rect.x, taskmgr[i].rect.y = tskpos[i][0]+a, tskpos[i][1]+b

	todo = 0
	for i in range(len(taskmgr)):
		if pygame.sprite.collide_rect(player, taskmgr[i]) == 1:
			todo = 1
			tasks.image = taskson
		else:
			tasks.image = tasksoff
	if todo == 1:
		tasks.image = taskson

	#dead
	dead = [(20, 100)]
	dead_grp = pygame.sprite.Group()
	reportbut = 0
	for i in range(len(dead)):
		ded = dead[i]
		dead[i] = Sprite(100, 100)
		dead[i].rect.x, dead[i].rect.y = ded[0]+a, ded[1]+b
		dead_grp.add(dead[i])

	dead_grp.draw(screen)
	for i in dead:
		if pygame.sprite.collide_rect(player, i) == 1:
			reportbut = 1
	if reportbut == 1:
		report.image = reporton
	else:
		report.image = reportoff

	for i in collision:
		if pygame.sprite.collide_rect(player, i):
			if keys[pygame.K_w]:
				if abs(player.rect.top - i.rect.bottom) < 10 and hit:
					b = before_pos[1]

			if keys[pygame.K_a]:
				if abs(player.rect.left - i.rect.right) < 10 and hit:
					a = before_pos[0]

			if keys[pygame.K_s]:
				if abs(player.rect.bottom - i.rect.top) < 10 and hit:
					b = before_pos[1]

			if keys[pygame.K_d]:
				if abs(player.rect.right - i.rect.left) < 10 and hit:
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

	a, b = coll

	#buttons
	#button_group.draw(screen)

	#screen.blit(kill, pygame.mouse.get_pos())

	num_players = 5

	totTasks += 0.1
	if totTasks>(num_players+1)*6 - 6:
		totTasks = 1

	'''pygame.draw.rect(screen, (0, 255, 0), (16, 19, totTasks*10, 30))
	for i in range(num_players):
		pygame.draw.rect(screen, (255, 255, 255), (16, 19, ((i+1)*6)*10, 30), 5)'''

	visible_points_x = []
	visible_points_y = []

	view = pygame.Surface.convert_alpha(pygame.Surface([1000, 550]))
	view.fill((0, 0, 0, 150))

	for i in range(255, 0, -1):
		pygame.draw.circle(view, (0,0,0,i), player.rect.center, i*3)

	for i in range(len(collision)):
		#print((coll_loc[i][0]+a, coll_loc[i][1]+b))
		if ((player.rect.center[0]-collision[i].rect.center[0])**2 + (player.rect.center[1]-collision[i].rect.center[1])**2)**(1/2) <= 250:
			try:
				#print((player.rect.center[1]-collision[i].rect.center[1])/(player.rect.center[0]-collision[i].rect.center[0]))
				#print(math.degrees(math.atan((player.rect.center[1]-collision[i].rect.center[1])/(player.rect.center[0]-collision[i].rect.center[0]))))
				#if math.degrees(math.atan((player.rect.center[1]-collision[i].rect.center[1])/(player.rect.center[0]-collision[i].rect.center[0]))) >= 0:
				if collision[i].rect.center[1] < player.rect.center[1]:
					pygame.draw.line(screen, (0, 255, 0), player.rect.center, (coll_loc[i][0]+a, coll_loc[i][1]+b))
					pygame.draw.line(screen, (0, 255, 0), player.rect.center, (coll_loc[i][0]+a+coll_loc[i][2], coll_loc[i][1]+b+coll_loc[i][3]))
					#visible_points_x.extend([(coll_loc[i][0]+a, coll_loc[i][1]+b), (coll_loc[i][0]+a+coll_loc[i][2], coll_loc[i][1]+b+coll_loc[i][3])])
				else:
					pygame.draw.line(screen, (0, 0, 255), player.rect.center, (coll_loc[i][0]+a, coll_loc[i][1]+b))
					pygame.draw.line(screen, (0, 0, 255), player.rect.center, (coll_loc[i][0]+a+coll_loc[i][2], coll_loc[i][1]+b+coll_loc[i][3]))
				visible_points_y.extend([(coll_loc[i][0]+a, coll_loc[i][1]+b), (coll_loc[i][0]+a+coll_loc[i][2], coll_loc[i][1]+b+coll_loc[i][3])])
				pygame.draw.polygon(view, (0, 255, 0, 0), (player.rect.center, (coll_loc[i][0]+a, coll_loc[i][1]+b), (coll_loc[i][0]+a+coll_loc[i][2], coll_loc[i][1]+b+coll_loc[i][3])))
				pygame.draw.polygon(view, (0, 255, 0, 0), (player.rect.center, (coll_loc[i][0]+a, coll_loc[i][1]+b), (coll_loc[i-1][0]+a, coll_loc[i-1][1]+b)))
				pygame.draw.polygon(view, (0, 255, 0, 0), (player.rect.center, (coll_loc[i][0]+a+coll_loc[i][2], coll_loc[i][1]+b+coll_loc[i][3]), (coll_loc[i+1][0]+a, coll_loc[i+1][1]+b)))

			except:
				pass

	"""for i in range(50, 0, -1):
		pygame.draw.circle(view, (0,0,0,i%2), player.rect.center, i*3)"""


	visible_points_x.extend(visible_points_y)

	#pygame.draw.polygon(view, (0,0,0,0), visible_points_x)

	screen.blit(view, (0, 0))
	wall_group.draw(screen)
	players.update()
	pygame.display.update()
	clock.tick(fps)
