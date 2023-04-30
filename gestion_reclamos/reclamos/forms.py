from django import forms
from django.forms.widgets import DateInput
from django.forms import widgets


class NuevoReclamo(forms.Form):
    urgencias = (
        (1, "Baja"),
        (2, "Media"),
        (3, "Alta"))
    
    calles = (
        (0, ""),
        (1, "12 de Octubre"),
        (2, "17 de Agosto"),
        (3, "20 de Junio"),
        (4, "25 de Mayo"),
        (5, "28 de Abril"),
        (6, "9 de Abril"),
        (7, "9 de Julio"),
        (8, "A. Crespo"),
        (9, "A. Dominguez"),
        (10, "Aceder"),
        (11, "Aconcagua"),
        (12, "Adolfo Alsina"),
        (13, "Adolfo Evaristo Negro"),
        (14, "Agente Jos? Montenegro"),
        (15, "Ag?ero (Ruta Prov.N? 16)"),
        (16, "Alejandro Burone Risso"),
        (17, "Alejandro Celestino Chir?n\r\nAlejandro Graham Bell"),
        (18, "Alejo Ortega"),
        (19, "Alfa Centauro"),
        (20, "Alf?rez Alberto Sardi"),
        (21, "Alf?rez E. A. Burlando"),
        (22, "Alf?rez Jos? Mar?a Sobral"),
        (23, "Alf?rez Rodrigo Mendiondo"),
        (24, "Alf?rez Rub?n Bertollo"),
        (25, "Alfonsina Storni"),
        (26, "Alfonso Amat"),
        (27, "Alfredo Sosa"),
        (28, "Almafuerte"),
        (29, "Almirante Brown"),
        (30, "Almirante Manuel Blanco Encalada"),
        (31, "Alvar Nu?ez\r"),
        (32, "Alvarez de Toledo"),
        (33, "Amado Nervo"),
        (34, "Andalgal?\r\nAndr?s Berasa?n\r"),
        (35, "Angel Tavagnutti"),
        (36, "Angela Gonz?lez de Barbier"),
        (37, "Anselmo S?enz Valiente"),
        (38, "Antofalla"),
        (39, "Antonio B. P?ez"),
        (40, "Antonio Cervetti"),
        (41, "Antonio Godoy Cruz"),
        (42, "Antonio Terrarosa"),
        (43, "Arist?teles"),
        (44, "Arq.Ricardo Adams"),
        (45, "Atl?ntida"),
        (46, "Av De Mayo"),
        (47, "Av. Fair"),
        (48, "Avda. Roberto Oliver"),
        (49, "Avenida Del Sur"),
        (50, "Ayacucho"),
        (51, "Azcu?naga"),
        (52, "Azul"),
        (53, "Bah?a Blanca"),
        (54, "Bah?a Esperanza"),
        (55, "Bah?a Thetis"),
        (56, "Balcarce"),
        (57, "Baldomero Fern?ndez Moreno"),
        (58, "Baliza Chiriguano"),
        (59, "Barracas"),
        (60, "Bartolom? De Las Casas"),
        (61, "Bel?n\r"),
        (62, "Benavidez"),
        (63, "Benito Sabato"),
        (64, "Benjam?n Vidal"),
        (65, "Bernardino Rivadavia"),
        (66, "Biarritz"),
        (67, "Bol?var"),
        (68, "Bonifacio Gifford"),
        (69, "Boulevard Buenos Aires"),
        (70, "Bragado"),
        (71, "Brandsen"),
        (72, "Brigadier Miguel Estanislao Soler"),
        (73, "Bristol"),
        (74, "Cabildo"),
        (75, "Cabo Corrientes"),
        (76, "Cabo San Antonio"),
        (77, "Cabo San Felipe"),
        (78, "Cabo San Jos?\r\nCacique Telomi?n Condi?\r\nCalle 13"),
        (79, "Calle 14"),
        (80, "Calle 4"),
        (81, "Calle 7"),
        (82, "CALLES"),
        (83, "Camino de Cintura"),
        (84, "Ca?uelas"),
        (85, "Capit?n Cairo"),
        (86, "Capit?n Jos? Madariaga"),
        (87, "Capit?n Justo Berm?dez"),
        (88, "Capit?n Moyano"),
        (89, "Capit?n Rosales"),
        (90, "Carlos Guido Spano"),
        (91, "Carlos Scaglia"),
        (92, "Carmen de Areco"),
        (93, "Catalina Berardi de Battipede"),
        (94, "Catamarca"),
        (95, "Cerro Catedral"),
        (96, "Cerro Mercedario"),
        (97, "Cerro San Javier"),
        (98, "Cerro Tronador"),
        (99, "Chacabuco"),
        (100, "Chivilcoy"),
        (101, "Cipr?s\r"),
        (102, "Ciudad de Cuzco"),
        (103, "Ciudad de Lima"),
        (104, "Colombia"),
        (105, "Colonia Monte Grande"),
        (106, "Comandante Tom?s Espora"),
        (107, "Comerciante Pedro Morando"),
        (108, "Comodoro Pedro Zanni"),
        (109, "Concejal Antonio Vidal"),
        (110, "Concejal Bartolom? L. Raffo"),
        (111, "Concejal Germ?n Palleros"),
        (112, "Constructor F?lix Chirio"),
        (113, "Cordero"),
        (114, "C?rdoba"),
        (115, "Cornelio Saavedra"),
        (116, "Coronel Alvaro Barros"),
        (117, "Coronel Juan R. Rojas"),
        (118, "Coronel Manuel Dorrego"),
        (119, "Coronel Pedro Regalado de la Plaza"),
        (120, "Coronel Pringles"),
        (121, "Coronel Vicente Dupuy"),
        (122, "Costa Rica"),
        (123, "Crist?bal Col?n\r\nCruz del Sur"),
        (124, "Cruz Montiel"),
        (125, "Cuba"),
        (126, "D. Jewet"),
        (127, "D'Elia"),
        (128, "Daireaux"),
        (129, "Daniel Defoe"),
        (130, "Dardo Rocha"),
        (131, "De La Noria"),
        (132, "De La Ribera"),
        (133, "De la Rivera"),
        (134, "De La Tradici?n\r\nDe Los Constituyentes"),
        (135, "Dean Funes"),
        (136, "Del Progreso"),
        (137, "Delfino"),
        (138, "Destacamento Melchor"),
        (139, "Diagonal Sur"),
        (140, "Dinamarca"),
        (141, "Dolores"),
        (142, "Dolores G. Ocantos"),
        (143, "Domador Jos? Chinivasi"),
        (144, "Domingo Chimondegui"),
        (145, "Domingo Faustino Sarmiento"),
        (146, "Domingo Matheu"),
        (147, "Don Cayetano Ugarteche"),
        (148, "Don Emilio Trotta"),
        (149, "Don Enrique Cayetano Caturini"),
        (150, "Don Jos? Mar?a Ignacio Mart?nez"),
        (151, "Don Leopoldo Mannucci"),
        (152, "Don Luis Trangoni"),
        (153, "Don Manuel Delorenzi"),
        (154, "Don Orione"),
        (155, "Don Segundo Sombra"),
        (156, "Do?a Mayor Humanes de Molina"),
        (157, "Dora Catalina Fleitas"),
        (158, "Dr Gilberto Francisco Elizalde"),
        (159, "Dr. Anacleto Rojas"),
        (160, "Dr. Angel Rotta"),
        (161, "Dr. E. Restelli"),
        (162, "Dr. Emilio Cardeza"),
        (163, "Dr. Guillermo Wilson"),
        (164, "Dr. Juan Garc?a del R?o\r"),
        (165, "Dr. Manuel Juli?n Medel"),
        (166, "Dr. Miguel Garc?a Fern?ndez"),
        (167, "Dr. Ren? Favaloro"),
        (168, "Dr.Antonio Montenegro"),
        (169, "Dr.Carlos Pellegrini"),
        (170, "Dr.Prof. Mariano Castex (Ruta Prov.58)"),
        (171, "Dra.Cecilia Grierson"),
        (172, "E. Banchs"),
        (173, "E. de Laperriere"),
        (174, "E. Recondo"),
        (175, "Edmundo De Amicis"),
        (176, "Eduardo Arana"),
        (177, "Eduardo Prayones"),
        (178, "Eduardo Wilde"),
        (179, "El Aguaribay"),
        (180, "El Amancay"),
        (181, "El Boyero"),
        (182, "El Ceibo"),
        (183, "El Chaj?\r\nEl Delta"),
        (184, "El Desv?o\r"),
        (185, "El Gaucho"),
        (186, "El Irup?\r\nEl Molino"),
        (187, "El Parten?n\r\nEl Resero"),
        (188, "El Salvador"),
        (189, "El Universo"),
        (190, "Emilio Lamarca"),
        (191, "Emilio Salgari"),
        (192, "Emilio Zol?\r\nEnrique Juan Roman?\r\nEnrique Santamar"),
        (193, "Entre R?os"),
        (194, "Escobar"),
        (195, "Escribano Francisco Vazquez"),
        (196, "Espa?a\r\nEsparta"),
        (197, "Esquel"),
        (198, "Estancia Los Remedios"),
        (199, "Estanislao Del Campo"),
        (200, "Esteban Echeverr?a\r"),
        (201, "Esteban G?mez"),
        (202, "Estevez"),
        (203, "Estrecho San Carlos"),
        (204, "Eugenio Rebizo"),
        (205, "Evaristo Carriego"),
        (206, "Evita"),
        (207, "Ezequiel Perez Iglesias"),
        (208, "F. Rodicio"),
        (209, "Facundo Quiroga"),
        (210, "Facundo Zuvir?a\r"),
        (211, "Faro 1? de Mayo"),
        (212, "Faro Patagonia"),
        (213, "Faro Recalada"),
        (214, "Fernando De Toro"),
        (215, "Ferrarotti"),
        (216, "Fitz Roy"),
        (217, "Florencio S?nchez"),
        (218, "Florentino Ameghino"),
        (219, "Florida"),
        (220, "Fortunato A. L?pez"),
        (221, "Fraga"),
        (222, "Fragata Hero?na"),
        (223, "Francisco Garc?a Romero"),
        (224, "Francisco Narciso de Laprida"),
        (225, "Francisco Zelada"),
        (226, "Fray Justo Santamar?a de Oro"),
        (227, "Fray Luis Beltr?n\r"),
        (228, "Fray Mamerto Esqui?"),
        (229, "French"),
        (230, "Gabriela Mistral"),
        (231, "Gamarra"),
        (232, "Garz?n\r\nGeneral Alvarado"),
        (233, "General Antonio Gonz?lez"),
        (234, "General Bartolom? Mitre"),
        (235, "General F?lix de Olazabal"),
        (236, "General Jos? M. Perez de Urdininea"),
        (237, "General Jos? M. Zapiola"),
        (238, "General Jos? Mar?a Paz"),
        (239, "General Las Heras"),
        (240, "General Lavalle"),
        (241, "General Manuel Nicol?s A. Savio"),
        (242, "General Rodr?guez"),
        (243, "General Rondeau"),
        (244, "General Tom?s Guido"),
        (245, "General Villegas"),
        (246, "Goleta Sarand?\r\nGolfo San Mat?as"),
        (247, "Gonz?lez Gowland"),
        (248, "Graciano Garriador"),
        (249, "Gral. Alvear"),
        (250, "Gral. Juan Andr?s Arenales"),
        (251, "Gral. Juan Domingo Per?n\r\nGranaderos"),
        (252, "Grecia"),
        (253, "Gregorio de Laferrere"),
        (254, "Guamin?\r\nGuatemala"),
        (255, "G?emes"),
        (256, "Guillermo Dickson"),
        (257, "Guillermo Enrique Hudson"),
        (258, "Guillermo Granado"),
        (259, "Henderson"),
        (260, "Hermanos Pinz?n\r\nHerminio Constanz?\r\nHernan Cort?s"),
        (261, "Hernandarias"),
        (262, "Hernando de Magallanes"),
        (263, "Hilario Ascasubi"),
        (264, "Hipolito Bouchard"),
        (265, "Hipolito Unanue"),
        (266, "Hipolito Yrigoyen"),
        (267, "Hoerth"),
        (268, "Homero"),
        (269, "Horacio T. Fischer"),
        (270, "Independencia"),
        (271, "Ingeniero Huergo"),
        (272, "Ingeniero Jorge Duclout"),
        (273, "Ingeniero Jos? A. Pettis"),
        (274, "Ingeniero Pedro J. Coni"),
        (275, "Intendente Agust?n Boul?n\r"),
        (276, "Intendente Celestino Galv?n\r"),
        (277, "Intendente Italiani"),
        (278, "Intendente Lucio Alfredo Lassalle"),
        (279, "Irup?\r\nIsaac Erasmo Rocha"),
        (280, "Isidoro Su?rez"),
        (281, "Isla Aguila"),
        (282, "Isla Coronaci?n\r\nIsla Decepci?n\r\nIsla Laurie"),
        (283, "Isla Mart?n Garc?a\r"),
        (284, "Isla Orcadas del Sur"),
        (285, "Isla San Jos?\r\nIsla Trinidad"),
        (286, "J. Recarte"),
        (287, "J.I. De La Rosa"),
        (288, "Joaqu?n Vicente Gonz?lez"),
        (289, "Jorge C?ceres Fortunato"),
        (290, "Jorge Miles"),
        (291, "Jorge Newbery"),
        (292, "Jos? A. Alvarez Condarco"),
        (293, "Jos? Hern?ndez"),
        (294, "Jos? Ingenieros"),
        (295, "Jos? L. Lemos"),
        (296, "Jos? M. Cabado"),
        (297, "Jos? Manuel Estrada"),
        (298, "Jos? M?rmol"),
        (299, "Jos? Mart?\r\nJuan Bautista Alberdi"),
        (300, "Juan Bautista Azopardo"),
        (301, "Juan Bautista Baigorria"),
        (302, "Juan Carlos Wieman"),
        (303, "Juan Casacuberta"),
        (304, "Juan Costallat"),
        (305, "Juan de Garay"),
        (306, "Juan D?az de Sol?s\r"),
        (307, "Juan Hern?ndez"),
        (308, "Juan Ignacio Madariaga"),
        (309, "Juan Jos? Castelli"),
        (310, "Juan J?se Paso"),
        (311, "Juan Larrea"),
        (312, "Juan Lorenzo Gerbi"),
        (313, "Juan Mandelli"),
        (314, "Juan Manuel Castro Chaves"),
        (315, "Juan Manuel de Rosas"),
        (316, "Juan Manuel Parente"),
        (317, "Juan Miguel Barberena"),
        (318, "Juan Schenzer"),
        (319, "Juan Sebasti?n Elcano"),
        (320, "Juan Tweedie"),
        (321, "Juan XXIII"),
        (322, "Juana de Arco"),
        (323, "Ju?rez"),
        (324, "Jujuy"),
        (325, "Juli?n Navarro"),
        (326, "Julio Argentino Roca"),
        (327, "Julio Verne"),
        (328, "Jun?n\r"),
        (329, "J?piter"),
        (330, "La batalla de Cepeda"),
        (331, "La Calandria"),
        (332, "La Costa"),
        (333, "La Horqueta"),
        (334, "La Iliada"),
        (335, "La Ni?a\r\nLa Odisea"),
        (336, "La Pampa"),
        (337, "La Pinta"),
        (338, "La Quinta"),
        (339, "La Rabida"),
        (340, "La Rioja"),
        (341, "La Santa Mar?a\r"),
        (342, "La Tierra"),
        (343, "Lago Argentino"),
        (344, "Lago Guti?rrez"),
        (345, "Lago Mascardi"),
        (346, "Lago Nahuel Huapi"),
        (347, "Lago Traful"),
        (348, "Lagos Garc?a\r"),
        (349, "Lan?s"),
        (350, "Larcam?n\r\nLas Azucenas"),
        (351, "Las Calas"),
        (352, "Las Cina Cinas"),
        (353, "Las Dalias"),
        (354, "Las Orqu?deas"),
        (355, "Las Rosas"),
        (356, "Las Talitas"),
        (357, "Las Violetas"),
        (358, "Lavard?n\r"),
        (359, "Leandro Nic?foro Alem"),
        (360, "Legarreta"),
        (361, "Leonardo Da Vinci"),
        (362, "Leopoldo Li?an\r"),
        (363, "Leopoldo Lugones"),
        (364, "Libertad"),
        (365, "Lincoln"),
        (366, "Liniers"),
        (367, "Lisandro De La Torre"),
        (368, "Lober?a\r"),
        (369, "Lobos"),
        (370, "Lola Mora"),
        (371, "Lorenzo Cresmani"),
        (372, "Los Alerces"),
        (373, "Los Andes"),
        (374, "Los Angeles"),
        (375, "Los Aromos"),
        (376, "Los Camalotes"),
        (377, "Los Cedros"),
        (378, "Los Claveles"),
        (379, "Los Jazm?nes"),
        (380, "Los Nogales"),
        (381, "Los Pinos"),
        (382, "Los Robles"),
        (383, "Los Tulipanes"),
        (384, "Luciano Valette"),
        (385, "Lucio Anneo S?neca"),
        (386, "Lucio Vicente L?pez"),
        (387, "Luis De Sarro"),
        (388, "Luis Guill?n\r\nLuis Pasteur"),
        (389, "Luis Vernet"),
        (390, "Luj?n\r"),
        (391, "M. Fitzgerald"),
        (392, "Magdalena"),
        (393, "Maip?"),
        (394, "Manuel Belgrano"),
        (395, "Manuel Cichero"),
        (396, "Manuel Wieman"),
        (397, "Mar del Plata"),
        (398, "Marcelino Lozano"),
        (399, "Marcos Sastre"),
        (400, "Mar?a Ester Balestrini de Lombardi"),
        (401, "Mar?a G.de Avila"),
        (402, "Mariana Arbel"),
        (403, "Mariano Acosta"),
        (404, "Mariano Alegre"),
        (405, "Mariano Moreno"),
        (406, "Marqu?s Alejandro Mar?a de Aguado"),
        (407, "Mart?n Coronado"),
        (408, "Mart?n Fierro"),
        (409, "Mart?n Hirigaray"),
        (410, "Mart?n Paulino Lacarra"),
        (411, "Mart?n Rivadavia"),
        (412, "Maximo Paz"),
        (413, "Mendoza"),
        (414, "Mercedario"),
        (415, "Mercedes"),
        (416, "Mercedes R. Sandoval"),
        (417, "Mercurio"),
        (418, "Miami"),
        (419, "Miguel Angel"),
        (420, "Miguel Angel Buonarrotti"),
        (421, "Miguel Can?\r\nMiguel Vidal"),
        (422, "Mi?ones"),
        (423, "Miranda"),
        (424, "Mois?s Mendez"),
        (425, "Monta?eses"),
        (426, "Monte Com?n\r"),
        (427, "Monte Guaran?\r\nMurguiondo"),
        (428, "Naum Kacowicz"),
        (429, "Navarro"),
        (430, "Neptuno"),
        (431, "Neuqu?n\r"),
        (432, "Nicaragua"),
        (433, "Nicol?s Avellaneda"),
        (434, "Nicol?s Bruzone"),
        (435, "Nicol?s Rodr?guez Pe?a\r\nNiza"),
        (436, "Norberto L?pez"),
        (437, "Nuestras Malvinas"),
        (438, "Nueva Escocia"),
        (439, "Oc?ano Atl?ntico"),
        (440, "Olavarr?a\r"),
        (441, "Olimpo"),
        (442, "Omega Petrazzini"),
        (443, "Pablo A. Pizzurno"),
        (444, "Pablo C?ceres"),
        (445, "Padre Mario Quadraccia"),
        (446, "Padre Pedro Milano"),
        (447, "Paran?\r\nParish Robertson"),
        (448, "Parque Los Glaciares"),
        (449, "Pastor Luna"),
        (450, "Patagones"),
        (451, "Patricios"),
        (452, "Paula Albarrac?n\r"),
        (453, "Pav?n\r\nPedro Alejandro Vargas"),
        (454, "Pedro Arocena"),
        (455, "Pedro Benjam?n Palacios"),
        (456, "Pedro Conde"),
        (457, "Pedro de Rocha"),
        (458, "Pedro Dreyer"),
        (459, "Pedro E. Legarto"),
        (460, "Pedro Faiat"),
        (461, "Pedro Farina"),
        (462, "Pedro Gandulfo"),
        (463, "Pedro Marinone"),
        (464, "Pedro Reta"),
        (465, "Pedro Suarez"),
        (466, "Pehuaj?\r\nPergamino"),
        (467, "Picquart"),
        (468, "Pila"),
        (469, "Pilar"),
        (470, "P?o XII"),
        (471, "Pje Armanino"),
        (472, "Plat?n\r\nPlaya de Castellamare"),
        (473, "Playa de Chapadmalal"),
        (474, "Playa de Claromec?\r\nPlaya de Copacabana"),
        (475, "Playa de Daytona"),
        (476, "Playa de La Paloma"),
        (477, "Playa de Miramar"),
        (478, "Playa de Monte Hermoso"),
        (479, "Playa de Necochea"),
        (480, "Playa de Ostende"),
        (481, "Playa de Pinamar"),
        (482, "Playa de Santa Margarita"),
        (483, "Plaza Huincul"),
        (484, "Plumerillo"),
        (485, "Plut?n\r\nPonce de Le?n\r\nPrebistero Orencio Antonio "),
        (486, "Preceptora Clementina Rend?n\r\nPrimera Junta"),
        (487, "Primo Tricotti"),
        (488, "Principado M?naco"),
        (489, "Procurador Mateo S?nchez"),
        (490, "Profesor Marxer"),
        (491, "Pu?n\r"),
        (492, "Puerto Argentino"),
        (493, "Puerto Deseado"),
        (494, "Puerto San Juli?n\r"),
        (495, "Puerto Soledad"),
        (496, "Pueyrred?n\r\nPunta del Este"),
        (497, "Punta Mogotes"),
        (498, "Punta Rassa"),
        (499, "Queirel"),
        (500, "Quintana"),
        (501, "Rafael De Sanzio"),
        (502, "Raimundo Mar?a Pisani"),
        (503, "Ramallo"),
        (504, "Ram?n Santamarina"),
        (505, "Ramos"),
        (506, "Rauch"),
        (507, "Raul Mazza"),
        (508, "Reconquista"),
        (509, "Remedios de Escalada de San Mart?n\r"),
        (510, "Rep?blica Argentina"),
        (511, "Rep?blica de Canad?\r\nRep?blica de Francia"),
        (512, "Rep?blica de Hait?\r\nRep?blica de Honduras"),
        (513, "Rep?blica de Panam?\r\nRep?blica de Per?"),
        (514, "Rep?blica del Paraguay"),
        (515, "Ricardo G?iraldes"),
        (516, "Ricardo Guti?rrez"),
        (517, "Ricardo Newton"),
        (518, "Ricardo Rojas"),
        (519, "R?o Gallegos"),
        (520, "R?o Grande"),
        (521, "R?o Limay"),
        (522, "R?o Quequ?n\r"),
        (523, "Riobamba"),
        (524, "Rivadavia"),
        (525, "Rivero"),
        (526, "Roberto Petracca"),
        (527, "Rodolfo Di Ci?\r\nRodolfo Pacinotti"),
        (528, "Roque Perez"),
        (529, "Rosario"),
        (530, "Rubens"),
        (531, "Rudecindo Alvarado"),
        (532, "Ruta de la Tradici?n (Ruta Prov.N?4)"),
        (533, "Saladillo"),
        (534, "Salta"),
        (535, "Salto"),
        (536, "San Antonio"),
        (537, "San Clemente del Tuy?"),
        (538, "San Fernando"),
        (539, "San Francisco de California"),
        (540, "San Juan"),
        (541, "San Luis"),
        (542, "San Mart?n\r"),
        (543, "San Miguel del Monte"),
        (544, "San Nicol?s\r"),
        (545, "San Pedrito"),
        (546, "San Remo"),
        (547, "San Sebasti?n\r"),
        (548, "Santa Adela"),
        (549, "Santa Bernardita"),
        (550, "Santa Catalina (Camino de Cintura)"),
        (551, "Santa Fe"),
        (552, "Santa In?s\r"),
        (553, "Santa Magdalena"),
        (554, "Santa Teresita"),
        (555, "Santiago Lumsden"),
        (556, "Santos Vega"),
        (557, "Sargento Juan Bautista Cabral"),
        (558, "Saturno"),
        (559, "Sebasti?n Gaboto"),
        (560, "Sebasti?n Maggio"),
        (561, "Siciliano"),
        (562, "Sierra de Ambato"),
        (563, "Sierra de Fiambal?\r\nSierra de Guasay?n\r"),
        (564, "Sierra de Velasco"),
        (565, "Sim?n G. Sansinena"),
        (566, "S?crates"),
        (567, "Sof?a Terrero de Santamarina"),
        (568, "Sorrento"),
        (569, "Sta. Rita"),
        (570, "Subteniente A. P. Gabaston"),
        (571, "Subteniente Alfredo O. Fox"),
        (572, "Subteniente Carlos Fader"),
        (573, "Subteniente Urbano Gonz?lez"),
        (574, "T. Ghersi"),
        (575, "Tacuar?\r\nTalcahuano"),
        (576, "Tandil"),
        (577, "Tapalqu?\r\nTeniente 1? Alberto Grande"),
        (578, "Teniente 1? Nicol?s Correa"),
        (579, "Teniente Benjam?n Matienzo"),
        (580, "Teniente Enrique Ins?a"),
        (581, "Teniente Evangelio G. Ford"),
        (582, "Teniente F. Bourquet"),
        (583, "Teniente General Ricchieri Pablo"),
        (584, "Teniente Jos? Pipo Giribone"),
        (585, "Teniente Manuel Origone"),
        (586, "Teniente Mariano Castex"),
        (587, "Teniente Mario Del Castillo"),
        (588, "Teniente Mart?n Retes"),
        (589, "Teniente Rub?n Ruiz"),
        (590, "Teresa Ariz Navarrette de Recarte"),
        (591, "Tesorero Jos? Tarulli"),
        (592, "Thom?s Alva Edison"),
        (593, "Tierra del Fuego"),
        (594, "Tilcara"),
        (595, "Tinogasta"),
        (596, "Tom?s Green"),
        (597, "Toribio de Luzuriaga"),
        (598, "Torquinst"),
        (599, "Trenque Lauqu?n\r"),
        (600, "Tres Arroyos"),
        (601, "Tres de Abril de 1889"),
        (602, "Triunvirato"),
        (603, "Tupungato"),
        (604, "Ubaldino Ortega"),
        (605, "Urano"),
        (606, "Urquiza"),
        (607, "Uruguay"),
        (608, "Valent?n Alsina"),
        (609, "Valladolid"),
        (610, "Ventura Avila"),
        (611, "Venus"),
        (612, "V?as de Ferrocarril"),
        (613, "Vicente L?pez"),
        (614, "Vicente Monti"),
        (615, "Vicente Torr? Sim?\r\nVilla Gesell"),
        (616, "Villarino"),
        (617, "Vi?a del Mar"),
        (618, "Volc?n Lan?n\r"),
        (619, "Yapey?"),
        (620, "Z?rate"),
        (621, "Calle 8"),
        (622, "calle 12"),
        (623, "Col?n\r\nBah?a San Juli?n\r"))
    
    localidadd = (
        (1, "Localidad 1"),
        (2, "Localidad 2"),
        (3, "Localidad 3"),
        (4, "Localidad 4"),
        (5, "Localidad 5"))
        
    
    numero = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número', 'required': True}))
    medio = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medio', 'required': True}))
    fuente = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fuente', 'required': True}))
    fecha = forms.DateField(widget=DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha', 'type': 'date', 'required': True}))

    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'required': True}))
    apellido = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido', 'required': True}))
    dni = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'DNI', 'required': True}))
    celular = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Celular', 'required': True}))
    telefono_fijo = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono fijo', 'required': True}))
    correo_electronico = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico', 'required': True}))

    calle = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Calle', 'required': True}), choices=calles)
    altura = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Altura', 'required': True}))
    edificio = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Edificio', 'required': True}))
    departamento = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Departamento', 'required': True}))
    entre_calle_1 = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Entre calle 1', 'required': True}), choices=calles)
    entre_calle_2 = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Entre calle 2', 'required': True}), choices=calles)
    localidad = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Localidad', 'required': True}))
    localidad = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Localidad', 'required': True}), choices=localidadd)
    reclamo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reclamo', 'required': True}))
    urgencia = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Urgencia'}), choices=urgencias)
    detalle = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Detalle', 'class': 'form-control', 'style': 'height: 10em;'}), required=False)