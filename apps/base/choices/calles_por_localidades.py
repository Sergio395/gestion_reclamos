from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


# 9 de Abril
class R2546787(TextChoices):
    BLANK = "", _("")
    CALLE_1 = "1", _("28 de Abril")
    CALLE_2 = "2", _("9 de Abril")
    CALLE_3 = "3", _("9 de Enero")
    CALLE_4 = "4", _("9 de Julio")
    CALLE_5 = "5", _("A. Paez")
    CALLE_6 = "6", _("Aconcagua")
    CALLE_7 = "7", _("Alfa Centauro")
    CALLE_8 = "8", _("Alfredo Lasalle")
    CALLE_9 = "9", _("Aristoteles")
    CALLE_10 = "10", _("Atlantida")
    CALLE_11 = "11", _("Avenida Doctor Gilberto Elizalde")
    CALLE_12 = "12", _("Avenida Luis Vernet")
    CALLE_13 = "13", _("Avenida Olimpo")
    CALLE_14 = "14", _("Avenida Roberto Oliver")
    CALLE_15 = "15", _("Avenida de Mayo")
    CALLE_16 = "16", _("Avenida de la Noria")
    CALLE_17 = "17", _("Avenida de la Ribera")
    CALLE_18 = "18", _("Avenida del Sur")
    CALLE_19 = "19", _("Azopardo")
    CALLE_20 = "20", _("B. Raffo")
    CALLE_21 = "21", _("Belen")
    CALLE_22 = "22", _("Biarritz")
    CALLE_23 = "23", _("Blanco Encalada")
    CALLE_24 = "24", _("Bouchard")
    CALLE_25 = "25", _("Bristol")
    CALLE_26 = "26", _("Cacique Telomian Condie")
    CALLE_27 = "27", _("Camino de la Ribera Sud")
    CALLE_28 = "28", _("Carlos Scaglia")
    CALLE_29 = "29", _("Castellamare")
    CALLE_30 = "30", _("Cerro Catedral")
    CALLE_31 = "31", _("Cerro San Javier")
    CALLE_32 = "32", _("Cerro Tronador")
    CALLE_33 = "33", _("Chapadmalal")
    CALLE_34 = "34", _("Colon")
    CALLE_35 = "35", _("Colonia Monte Grande")
    CALLE_36 = "36", _("Comandante Espora")
    CALLE_37 = "37", _("Copacabana")
    CALLE_38 = "38", _("Coronel Alvaro Barros")
    CALLE_39 = "39", _("Cruz Montiel")
    CALLE_40 = "40", _("Cruz del Sur")
    CALLE_41 = "41", _("Daniel Defoe")
    CALLE_42 = "42", _("Daytona")
    CALLE_43 = "43", _("Del Progreso")
    CALLE_44 = "44", _("Doctor Ernesto Restelli")
    CALLE_45 = "45", _("Domingo Chimondegui")
    CALLE_46 = "46", _("Don Segundo Sombra")
    CALLE_47 = "47", _("Edmundo D'Amicis")
    CALLE_48 = "48", _("El Gaucho")
    CALLE_49 = "49", _("El Partenon")
    CALLE_50 = "50", _("El Resero")
    CALLE_51 = "51", _("Emilio Salgari")
    CALLE_52 = "52", _("Emilio Zola")
    CALLE_53 = "53", _("Esparta")
    CALLE_54 = "54", _("Esteban Echeverria")
    CALLE_55 = "55", _("Eusebio Rebizo")
    CALLE_56 = "56", _("Felix Picquart")
    CALLE_57 = "57", _("Fortunato Lopez")
    CALLE_58 = "58", _("General Jose Marinzio")
    CALLE_59 = "59", _("Remedios de Escalada de San Martin")
    CALLE_60 = "60", _("Republica del Peru")
    CALLE_61 = "61", _("Ruta de la Tradicion")
    CALLE_62 = "62", _("Saenz Valiente")
    CALLE_63 = "63", _("San Agustin")
    CALLE_64 = "64", _("San Andres")
    CALLE_65 = "65", _("San Antonio")
    CALLE_66 = "66", _("San Clemente del Tuyu")
    CALLE_67 = "67", _("San Fernando")
    CALLE_68 = "68", _("San Francisco de California")
    CALLE_69 = "69", _("San Joaquin")
    CALLE_70 = "70", _("San Juan")
    CALLE_71 = "71", _("San Lucas")
    CALLE_72 = "72", _("San Nicolas")
    CALLE_73 = "73", _("San Pedro")
    CALLE_74 = "74", _("San Remo")
    CALLE_75 = "75", _("San Sebastian")
    CALLE_76 = "76", _("Santa Adela")
    CALLE_77 = "77", _("Santa Ana")
    CALLE_78 = "78", _("Santa Bernardita")
    CALLE_79 = "79", _("Santa Ines")
    CALLE_80 = "80", _("Santa Magdalena")
    CALLE_81 = "81", _("Santa Margarita")
    CALLE_82 = "82", _("Santa Rita")
    CALLE_83 = "83", _("Santa Teresita")
    CALLE_84 = "84", _("Santiago Lumsden")
    CALLE_85 = "85", _("Santos Vega")
    CALLE_86 = "86", _("Sargento Mayor Jose Leon Lemos")
    CALLE_87 = "87", _("Saturno")
    CALLE_88 = "88", _("Sebastian Elcano")
    CALLE_89 = "89", _("Sebastian Gaboto")
    CALLE_90 = "90", _("Sierra De Velazco")
    CALLE_91 = "91", _("Sierra de Ambato")
    CALLE_92 = "92", _("Sierra de Fiambala")
    CALLE_93 = "93", _("Sierra de Guasaya")
    CALLE_94 = "94", _("Sierra de Velazco")
    CALLE_95 = "95", _("Simon Sansinena")
    CALLE_96 = "96", _("Socrates")
    CALLE_97 = "97", _("Sorrento")
    CALLE_98 = "98", _("Teniente Enrique Insua")
    CALLE_99 = "99", _("Teniente Joaquin Castex")
    CALLE_100 = "100", _("Tupungato")
    CALLE_101 = "101", _("Urano")
    CALLE_102 = "102", _("Valladolid")
    CALLE_103 = "103", _("Venus")
    CALLE_104 = "104", _("Villa Gesell")
    CALLE_105 = "105", _("Vina del Mar")
    CALLE_106 = "106", _("Volcan Lanin")


# Canning
class R2546804(TextChoices):
    BLANK = "", _("")
    CALLE_1 = "1", _("Agustin Boulan")
    CALLE_2 = "2", _("Alejandro Graham Bell")
    CALLE_3 = "3", _("Alfredo Sosa")
    CALLE_4 = "4", _("Alvarez de Toledo")
    CALLE_5 = "5", _("Avenida Mariano Castex")
    CALLE_6 = "6", _("Avenida Pedro Dreyer")
    CALLE_7 = "7", _("Avenida Sargento Cabral")
    CALLE_8 = "8", _("Boulevard Dupuy")
    CALLE_9 = "9", _("Boulevard Saint Thomas")
    CALLE_10 = "10", _("Chiron")
    CALLE_11 = "11", _("Cuba")
    CALLE_12 = "12", _("Escribano Francissco Vazquez")
    CALLE_13 = "13", _("Fortunato Caceres")
    CALLE_14 = "14", _("Gral. Antonio Gonzalez")
    CALLE_15 = "15", _("Isidoro Suarez")
    CALLE_16 = "16", _("Jose Ignacio De La Rosa")
    CALLE_17 = "17", _("Juan Martin de Pueyrredon")
    CALLE_18 = "18", _("Juana de Arco")
    CALLE_19 = "19", _("Lacarra")
    CALLE_20 = "20", _("Lago Argentino")
    CALLE_21 = "21", _("Lago Mascardi")
    CALLE_22 = "22", _("Libertad")
    CALLE_23 = "23", _("M. Vidal")
    CALLE_24 = "24", _("Martin Fierro")
    CALLE_25 = "25", _("Miguel Angel")
    CALLE_26 = "26", _("Neuquen")
    CALLE_27 = "27", _("Olavarria")
    CALLE_28 = "28", _("Parana")
    CALLE_29 = "29", _("Pedro Arocena")
    CALLE_30 = "30", _("Pedro Marione")
    CALLE_31 = "31", _("Republica de Costa Rica")
    CALLE_32 = "32", _("Republica de Cuba")
    CALLE_33 = "33", _("Republica de Nicaragua")
    CALLE_34 = "34", _("Republica de Panama")
    CALLE_35 = "35", _("Rio Limay")
    CALLE_36 = "36", _("Ruta Provincial 58")
    CALLE_37 = "37", _("Talcahuano")
    CALLE_38 = "38", _("Teniente Jose 'Pipo' Giribone")


# El Jagüel
class R2546834(TextChoices):
    BLANK = "", _("")
    CALLE_1 = "1", _("12 de Octubre")
    CALLE_2 = "2", _("17 de Agosto")
    CALLE_3 = "3", _("20 de Junio")
    CALLE_4 = "4", _("25 de Mayo")
    CALLE_5 = "5", _("Almafuerte")
    CALLE_6 = "6", _("Amado Nervo")
    CALLE_7 = "7", _("Andalgala")
    CALLE_8 = "8", _("Andres Berasain")
    CALLE_9 = "9", _("Angel Rotta")
    CALLE_10 = "10", _("Angela Gonzalez de Barbieri")
    CALLE_11 = "11", _("Antonio Cervetti")
    CALLE_12 = "12", _("Antonio Crespo")
    CALLE_13 = "13", _("Antonio Delfino")
    CALLE_14 = "14", _("Antonio Terrarosa")
    CALLE_15 = "15", _("Arenales")
    CALLE_16 = "16", _("Autopista Ezeiza - Canuelas")
    CALLE_17 = "17", _("Avenida Dardo Rocha")
    CALLE_18 = "18", _("Avenida Jorge Newbery")
    CALLE_19 = "19", _("Avenida Julio Argentino Roca")
    CALLE_20 = "20", _("Avenida Mariano Castex")
    CALLE_21 = "21", _("Avenida Pedro Dreyer")
    CALLE_22 = "22", _("Avenida V. Fair")
    CALLE_23 = "23", _("Bahia Esperanza")
    CALLE_24 = "24", _("Baliza Chiriguano")
    CALLE_25 = "25", _("Cabildo")
    CALLE_26 = "26", _("Cabo San Antonio")
    CALLE_27 = "27", _("Cabo San Jose")
    CALLE_28 = "28", _("Camalotes")
    CALLE_29 = "29", _("Catamarca")
    CALLE_30 = "30", _("Cichero")
    CALLE_31 = "31", _("Cornelio Saavedra")
    CALLE_32 = "32", _("Costa Rica")
    CALLE_33 = "33", _("Dardo Rocha")
    CALLE_34 = "34", _("Dean Funes")
    CALLE_35 = "35", _("Destacamento Melchor")
    CALLE_36 = "36", _("Diagonal Sur")
    CALLE_37 = "37", _("Doctor Manuel Julian Medel")
    CALLE_38 = "38", _("Domingo Matheu")
    CALLE_39 = "39", _("El Aguaribay")
    CALLE_40 = "40", _("El Amancay")
    CALLE_41 = "41", _("El Boyero")
    CALLE_42 = "42", _("El Ceibo")
    CALLE_43 = "43", _("El Chaja")
    CALLE_44 = "44", _("El Desvio")
    CALLE_45 = "45", _("El Irupe")
    CALLE_46 = "46", _("El Molino")
    CALLE_47 = "47", _("Emilio Trotta")
    CALLE_48 = "48", _("Emilio de Laperriere")
    CALLE_49 = "49", _("Enrique Santamarina")
    CALLE_50 = "50", _("Entre Rios")
    CALLE_51 = "51", _("Estancia Los Remedios")
    CALLE_52 = "52", _("Evita")
    CALLE_53 = "53", _("Faro Patagonia")
    CALLE_54 = "54", _("Faro Primero de Mayo")
    CALLE_55 = "55", _("Faro Recalada")
    CALLE_56 = "56", _("Fernandez Moreno")
    CALLE_57 = "57", _("Fernando de Toro")
    CALLE_58 = "58", _("Florencio Sanchez")
    CALLE_59 = "59", _("Francisco Narciso de Laprida")
    CALLE_60 = "60", _("Fray Luis Beltran")
    CALLE_61 = "61", _("Fray Mamerto Esquiu")
    CALLE_62 = "62", _("General Bartolome Mitre")
    CALLE_63 = "63", _("Golfo San Matias")
    CALLE_64 = "64", _("Gregorio de La Ferrere")
    CALLE_65 = "65", _("Guarani")
    CALLE_66 = "66", _("Guido Spano")
    CALLE_67 = "67", _("Hipolito Bouchard")
    CALLE_68 = "68", _("Isla Decepcion")
    CALLE_69 = "69", _("Isla Martin Garcia")
    CALLE_70 = "70", _("Isla Trinidad")
    CALLE_71 = "71", _("Islas Orcadas del Sur")
    CALLE_72 = "72", _("Italiani")
    CALLE_73 = "73", _("Joaquin Gonzalez")
    CALLE_74 = "74", _("Jorge Newbery")
    CALLE_75 = "75", _("Jose Ingenieros")
    CALLE_76 = "76", _("Jose Manuel Estrada")
    CALLE_77 = "77", _("Jose Marmol")
    CALLE_78 = "78", _("Juan Hernandez")
    CALLE_79 = "79", _("Juan Miguel Barberena")
    CALLE_80 = "80", _("Julio Argentino Roca")
    CALLE_81 = "81", _("Justo Santa Maria de Oro")
    CALLE_82 = "82", _("La Calandria")
    CALLE_83 = "83", _("La Horqueta")
    CALLE_84 = "84", _("La Rioja")
    CALLE_85 = "85", _("Lanus")
    CALLE_86 = "86", _("Las Cina Cinas")
    CALLE_87 = "87", _("Leonardo da Vinci")
    CALLE_88 = "88", _("Leopoldo Lugones")
    CALLE_89 = "89", _("Los Alerces")
    CALLE_90 = "90", _("Los Nogales")
    CALLE_91 = "91", _("Los Pinos")
    CALLE_92 = "92", _("Los Robles")
    CALLE_93 = "93", _("Mamerto Esquiu")
    CALLE_94 = "94", _("Manuel Cichero")
    CALLE_95 = "95", _("Mariano Acosta")
    CALLE_96 = "96", _("Marques de Aguado")
    CALLE_97 = "97", _("Martin Fierro")
    CALLE_98 = "98", _("Maximo Paz")
    CALLE_99 = "99", _("Meliton Legarreta")
    CALLE_100 = "100", _("Miguel Angel")
    CALLE_101 = "101", _("Norberto Lopez")
    CALLE_102 = "102", _("Pablo Pizzurno")
    CALLE_103 = "103", _("Pedro Gandulfo")
    CALLE_104 = "104", _("Pedro Marione")
    CALLE_105 = "105", _("Pedro Milano")
    CALLE_106 = "106", _("Pedro Palacios")
    CALLE_107 = "107", _("Pio XII")
    CALLE_108 = "108", _("Presidente Quintana")
    CALLE_109 = "109", _("Punta Mogotes")
    CALLE_110 = "110", _("Punta Rassa")
    CALLE_111 = "111", _("Quiroga")
    CALLE_112 = "112", _("Ramon Santamarina")
    CALLE_113 = "113", _("Republica de Colombia")
    CALLE_114 = "114", _("Republica de Cuba")
    CALLE_115 = "115", _("Republica de Nicaragua")
    CALLE_116 = "116", _("Republica de Panama")
    CALLE_117 = "117", _("Republica de Paraguay")
    CALLE_118 = "118", _("Ricardo Guiraldes")
    CALLE_119 = "119", _("Ricardo Gutierrez")
    CALLE_120 = "120", _("Ricardo Newton")
    CALLE_121 = "121", _("Riobamba")
    CALLE_122 = "122", _("Risso")
    CALLE_123 = "123", _("Rubens")
    CALLE_124 = "124", _("San Felipe")
    CALLE_125 = "125", _("San Lorenzo")
    CALLE_126 = "126", _("San Luis")
    CALLE_127 = "127", _("Santa Fe")
    CALLE_128 = "128", _("Tilcara")
    CALLE_129 = "129", _("Tomas Alva Edison")
    CALLE_130 = "130", _("Ugarteche")
    CALLE_131 = "131", _("Valentin Alsina")
    CALLE_132 = "132", _("Valentina Alsina")
    CALLE_133 = "133", _("Vidal")
    CALLE_134 = "134", _("Yapeyu")


# Luis Guillón
class R2546803(TextChoices):
    BLANK = "", _("")
    CALLE_1 = "1", _("A. Vidal")
    CALLE_2 = "2", _("Alf. Varisco")
    CALLE_3 = "3", _("Alferez Alberto Sardi")
    CALLE_4 = "4", _("Alferez Burlando")
    CALLE_5 = "5", _("Alferez Rodrigo Mendiondo")
    CALLE_6 = "6", _("Alferez Ruben Bertollo")
    CALLE_7 = "7", _("Almafuerte")
    CALLE_8 = "8", _("Antonio Dominguez")
    CALLE_9 = "9", _("Arquitecto Richard Adams")
    CALLE_10 = "10", _("Avenida Facundo Zuviria")
    CALLE_11 = "11", _("Avenida Luciano Valette")
    CALLE_12 = "12", _("Avenida Nicolas Bruzone")
    CALLE_13 = "13", _("Avenida Pedro Suarez")
    CALLE_14 = "14", _("Avenida Pedro Suarez (EE) / Capitan de Fragata Moyano (AB)")
    CALLE_15 = "15", _("Benjamin Matienzo")
    CALLE_16 = "16", _("Bonifacio Gifford")
    CALLE_17 = "17", _("Boulevard Buenos Aires")
    CALLE_18 = "18", _("Brigadier General Juan Manuel de Rosas")
    CALLE_19 = "19", _("Camino de Cintura")
    CALLE_20 = "20", _("Canada")
    CALLE_21 = "21", _("Capitan Claudio Rosales")
    CALLE_22 = "22", _("Celina Grierson")
    CALLE_23 = "23", _("Cepeda")
    CALLE_24 = "24", _("Chacabuco")
    CALLE_25 = "25", _("Chirio")
    CALLE_26 = "26", _("Colectora RP4")
    CALLE_27 = "27", _("Colonia Monte Grande")
    CALLE_28 = "28", _("Cordoba")
    CALLE_29 = "29", _("Coronel Alvaro Barros")
    CALLE_30 = "30", _("Costa Rica")
    CALLE_31 = "31", _("De los Constituyentes")
    CALLE_32 = "32", _("Doctor Emilio Cardeza")
    CALLE_33 = "33", _("Doctor Rene Favaloro")
    CALLE_34 = "34", _("Don Luis Trangoni")
    CALLE_35 = "35", _("Dora Catalina Fleitas")
    CALLE_36 = "36", _("Eduardo Arana")
    CALLE_37 = "37", _("Espana")
    CALLE_38 = "38", _("Estevez")
    CALLE_39 = "39", _("Estrecho San Carlos")
    CALLE_40 = "40", _("Florentino Ameghino")
    CALLE_41 = "41", _("Francia")
    CALLE_42 = "42", _("Garzon")
    CALLE_43 = "43", _("Guatemala")
    CALLE_44 = "44", _("Guillermo Dickson")
    CALLE_45 = "45", _("Guillermo Wilson")
    CALLE_46 = "46", _("H. Fischer")
    CALLE_47 = "47", _("Haiti")
    CALLE_48 = "48", _("Hilario Ascasubi")
    CALLE_49 = "49", _("Hipolito Yrigoyen")
    CALLE_50 = "50", _("Honduras")
    CALLE_51 = "51", _("Independencia")
    CALLE_52 = "52", _("Intendente Celestino Galvan")
    CALLE_53 = "53", _("Joaquin Victor Gonzalez")
    CALLE_54 = "54", _("Jorge Miles")
    CALLE_55 = "55", _("Jorge Newbery")
    CALLE_56 = "56", _("Jose Hernandez")
    CALLE_57 = "57", _("Jose Madariaga")
    CALLE_58 = "58", _("Juan Bautista Alberdi")
    CALLE_59 = "59", _("Juan Carlos Wieman")
    CALLE_60 = "60", _("Juan Tweedie")
    CALLE_61 = "61", _("Juan Varisco")
    CALLE_62 = "62", _("Juan de Garay")
    CALLE_63 = "63", _("Jujuy")
    CALLE_64 = "64", _("Lagos Garcia")
    CALLE_65 = "65", _("Las Talitas")
    CALLE_66 = "66", _("Lima")
    CALLE_67 = "67", _("Liniers")
    CALLE_68 = "68", _("Lisandro de La Torre")
    CALLE_69 = "69", _("Los Aromos")
    CALLE_70 = "70", _("Luis de Sarro")
    CALLE_71 = "71", _("Magallanes")
    CALLE_72 = "72", _("Manuel Belgrano")
    CALLE_73 = "73", _("Maria Esther Balestrini de Lombardi")
    CALLE_74 = "74", _("Mariana Arbel")
    CALLE_75 = "75", _("Mariano Moreno")
    CALLE_76 = "76", _("Martin Coronado")
    CALLE_77 = "77", _("Mendoza")
    CALLE_78 = "78", _("Miguel Angel")
    CALLE_79 = "79", _("Nicaragua")
    CALLE_80 = "80", _("Nicolas Avellaneda")
    CALLE_81 = "81", _("Nicolas Correa")
    CALLE_82 = "82", _("Nueva Escocia")
    CALLE_83 = "83", _("Parish Robertson")
    CALLE_84 = "84", _("Pavon")
    CALLE_85 = "85", _("Pedro Faiat")
    CALLE_86 = "86", _("Pedro Zanni")
    CALLE_87 = "87", _("Pedro de Rocha")
    CALLE_88 = "88", _("Ponce de Leon")
    CALLE_89 = "89", _("Primo Tricotti")
    CALLE_90 = "90", _("Profesor Marxer")
    CALLE_91 = "91", _("Puerto Deseado")
    CALLE_92 = "92", _("Rafael de Sanzio")
    CALLE_93 = "93", _("Reconquista")
    CALLE_94 = "94", _("Republica Argentina")
    CALLE_95 = "95", _("Ricardo Rojas")
    CALLE_96 = "96", _("Roberto Petracca")
    CALLE_97 = "97", _("Rodolfo Pachinotti")
    CALLE_98 = "98", _("Rotonda de Llavallol")
    CALLE_99 = "99", _("Ruta de la Tradicion")
    CALLE_100 = "100", _("San Martin")
    CALLE_101 = "101", _("San Nicolas")
    CALLE_102 = "102", _("Santa Catalina")
    CALLE_103 = "103", _("Sastre")
    CALLE_104 = "104", _("Savio")
    CALLE_105 = "105", _("Sebastian Maggio")
    CALLE_106 = "106", _("Siciliano")
    CALLE_107 = "107", _("Subteniente Alfredo Fox")
    CALLE_108 = "108", _("Subteniente Antonio Gabaston")
    CALLE_109 = "109", _("Subteniente Carlos Fader")
    CALLE_110 = "110", _("Subteniente Gamarra")
    CALLE_111 = "111", _("Subteniente Urbano Gonzalez")
    CALLE_112 = "112", _("Tacuari")
    CALLE_113 = "113", _("Tarulli")
    CALLE_114 = "114", _("Teniente Evangelino G. Ford")
    CALLE_115 = "115", _("Teniente Felix Bourquet")
    CALLE_116 = "116", _("Teniente Mario Agustin del Castillo")
    CALLE_117 = "117", _("Teniente Martin Retes")
    CALLE_118 = "118", _("Teniente O. Larcamon")
    CALLE_119 = "119", _("Teniente Primero Alberto Grande")
    CALLE_120 = "120", _("Teniente Ruben Ruiz")
    CALLE_121 = "121", _("Urbano Gonzalez")
    CALLE_122 = "122", _("Urquiza")
    CALLE_123 = "123", _("Wilde")


# Monte Grande
class R2546842(TextChoices):
    BLANK = "", _("")
    CALLE_1 = "1", _("12 de Octubre")
    CALLE_2 = "2", _("25 de Mayo")
    CALLE_3 = "3", _("9 de Abril")
    CALLE_4 = "4", _("9 de Julio")
    CALLE_5 = "5", _("Adolfo Alsina")
    CALLE_6 = "6", _("Alejo Ortega")
    CALLE_7 = "7", _("Alferez Alberto Sardi")
    CALLE_8 = "8", _("Alfonsina Storni")
    CALLE_9 = "9", _("Alfonso Amat")
    CALLE_10 = "10", _("Alfonso Amat (EE) / Avenida Argentina (AB)")
    CALLE_11 = "11", _("Almirante Brown")
    CALLE_12 = "12", _("Almirante Cordero")
    CALLE_13 = "13", _("Alvar Nunez")
    CALLE_14 = "14", _("Amado Nervo")
    CALLE_15 = "15", _("Anacleto Rojas")
    CALLE_16 = "16", _("Andres Berasain")
    CALLE_17 = "17", _("Angela Gonzalez de Barbieri")
    CALLE_18 = "18", _("Antonio Cervetti")
    CALLE_19 = "19", _("Antonio Crespo")
    CALLE_20 = "20", _("Antonio Rivero")
    CALLE_21 = "21", _("Antonio Terrarosa")
    CALLE_22 = "22", _("Arenales")
    CALLE_23 = "23", _("Avenida Argentina")
    CALLE_24 = "24", _("Avenida Dardo Rocha")
    CALLE_25 = "25", _("Avenida Enrique Santamarina")
    CALLE_26 = "26", _("Avenida Facundo Zuviria")
    CALLE_27 = "27", _("Avenida Fitz Roy")
    CALLE_28 = "28", _("Avenida Julio Argentino Roca")
    CALLE_29 = "29", _("Avenida Luciano Valette")
    CALLE_30 = "30", _("Avenida Luis Vernet")
    CALLE_31 = "31", _("Avenida Nicolas Bruzone")
    CALLE_32 = "32", _("Avenida Pedro Dreyer")
    CALLE_33 = "33", _("Avenida Pedro Suarez")
    CALLE_34 = "34", _("Avenida Pedro Suarez (EE) / Capitan de Fragata Moyano (AB)")
    CALLE_35 = "35", _("Avenida Roberto Oliver")
    CALLE_36 = "36", _("Avenida V. Fair")
    CALLE_37 = "37", _("Avila")
    CALLE_38 = "38", _("Ayacucho")
    CALLE_39 = "39", _("Azcuenaga")
    CALLE_40 = "40", _("Azul")
    CALLE_41 = "41", _("B. Raffo")
    CALLE_42 = "42", _("B. Vidal")
    CALLE_43 = "43", _("Bahia Blanca")
    CALLE_44 = "44", _("Bahia San Julian")
    CALLE_45 = "45", _("Bahia Thetis")
    CALLE_46 = "46", _("Balcarce")
    CALLE_47 = "47", _("Baliza Chiriguano")
    CALLE_48 = "48", _("Barracas")
    CALLE_49 = "49", _("Benito Sabato")
    CALLE_50 = "50", _("Benjamin Matienzo")
    CALLE_51 = "51", _("Bolivar")
    CALLE_52 = "52", _("Bolivar")
    CALLE_53 = "53", _("Bonifacio Gifford")
    CALLE_54 = "54", _("Boulevard Buenos Aires")
    CALLE_55 = "55", _("Brigadier Miguel Estanislao de Soler")
    CALLE_56 = "56", _("Cabo Corrientes")
    CALLE_57 = "57", _("Cabo San Felipe")
    CALLE_58 = "58", _("Calle 1")
    CALLE_59 = "59", _("Calle 10")
    CALLE_60 = "60", _("Calle 11")
    CALLE_61 = "61", _("Calle 12")
    CALLE_62 = "62", _("Calle 13")
    CALLE_63 = "63", _("Calle 14")
    CALLE_64 = "64", _("Calle 15")
    CALLE_65 = "65", _("Calle 2")
    CALLE_66 = "66", _("Calle 3")
    CALLE_67 = "67", _("Calle 4")
    CALLE_68 = "68", _("Calle 5")
    CALLE_69 = "69", _("Calle 7")
    CALLE_70 = "70", _("Calle 8")
    CALLE_71 = "71", _("Calle 9")
    CALLE_72 = "72", _("Calle-")
    CALLE_73 = "73", _("Camino de las Latas")
    CALLE_74 = "74", _("Capitan Cairo")
    CALLE_75 = "75", _("Carlos Pellegrini")
    CALLE_76 = "76", _("Carlos Scaglia")
    CALLE_77 = "77", _("Carmen de Areco")
    CALLE_78 = "78", _("Casacuberta")
    CALLE_79 = "79", _("Castelli")
    CALLE_80 = "80", _("Catalina Berardi de Battipede")
    CALLE_81 = "81", _("Caturini")
    CALLE_82 = "82", _("Cepeda")
    CALLE_83 = "83", _("Cerro Catedral")
    CALLE_84 = "84", _("Chacabuco")
    CALLE_85 = "85", _("Chinivasi")
    CALLE_86 = "86", _("Cipres")
    CALLE_87 = "87", _("Cordoba")
    CALLE_88 = "88", _("Cornelio Saavedra")
    CALLE_89 = "89", _("Coronel Alvaro Barros")
    CALLE_90 = "90", _("Coronel D'Elia")
    CALLE_91 = "91", _("Coronel Manuel Dorrego")
    CALLE_92 = "92", _("Cristobal Colon")
    CALLE_93 = "93", _("Daireaux")
    CALLE_94 = "94", _("Dean Funes")
    CALLE_95 = "95", _("Delfino")
    CALLE_96 = "96", _("Dinamarca")
    CALLE_97 = "97", _("Doctor Angel Rotta")
    CALLE_98 = "98", _("Doctor Emilio Cardeza")
    CALLE_99 = "99", _("Doctor Manuel Julian Medel")
    CALLE_100 = "100", _("Dolores")
    CALLE_101 = "101", _("Dolores Gonzalez Ocantos")
    CALLE_102 = "102", _("Domingo Chimondegui")
    CALLE_103 = "103", _("Domingo Faustino Sarmiento")
    CALLE_104 = "104", _("Don Orione")
    CALLE_105 = "105", _("Don Vicente Torro Simo")
    CALLE_106 = "106", _("Dona Mayor Humanes de Molina")
    CALLE_107 = "107", _("Eduardo Arana")
    CALLE_108 = "108", _("El Ceibo")
    CALLE_109 = "109", _("El Jacaranda")
    CALLE_110 = "110", _("Emilio M. De Laperriere")
    CALLE_111 = "111", _("Emilio de Laperriere")
    CALLE_112 = "112", _("Enrique Banchs")
    CALLE_113 = "113", _("Entre Rios")
    CALLE_114 = "114", _("Escobar")
    CALLE_115 = "115", _("Escribano R. Di Cio")
    CALLE_116 = "116", _("Escribano Rodolfo Di Cio")
    CALLE_117 = "117", _("Esquel")
    CALLE_118 = "118", _("Estanislao del Campo")
    CALLE_119 = "119", _("Esteban Echeverria")
    CALLE_120 = "120", _("Esteban Gomez")
    CALLE_121 = "121", _("Estrecho San Carlos")
    CALLE_122 = "122", _("Eugenio Rebizo")
    CALLE_123 = "123", _("Eusebio Rebizo")
    CALLE_124 = "124", _("Evaristo Carriego")
    CALLE_125 = "125", _("Evita")
    CALLE_126 = "126", _("Ezequiel Perez Iglesias")
    CALLE_127 = "127", _("F Rodicio")
    CALLE_128 = "128", _("Faro Patagonia")
    CALLE_129 = "129", _("Faro Primero de Mayo")
    CALLE_130 = "130", _("Fernando de Toro")
    CALLE_131 = "131", _("Florencio Sanchez")
    CALLE_132 = "132", _("Florentino Ameghino")
    CALLE_133 = "133", _("Florida")
    CALLE_134 = "134", _("Fortunato Caceres")
    CALLE_135 = "135", _("Fortunato Lopez")
    CALLE_136 = "136", _("Fraga")
    CALLE_137 = "137", _("Francisco Garcia Romero")
    CALLE_138 = "138", _("Francisco Narciso de Laprida")
    CALLE_139 = "139", _("Francisco Recondo")
    CALLE_140 = "140", _("Fray Luis Beltran")
    CALLE_141 = "141", _("Fregata Heroina")
    CALLE_142 = "142", _("French")
    CALLE_143 = "143", _("Gabriela Mistral")
    CALLE_144 = "144", _("Garzon")
    CALLE_145 = "145", _("General Alvarado")
    CALLE_146 = "146", _("General Alvear")
    CALLE_147 = "147", _("General Bartolome Mitre")
    CALLE_148 = "148", _("General Carlos Alvear")
    CALLE_149 = "149", _("General Jose Rondeau")
    CALLE_150 = "150", _("General Las Heras")
    CALLE_151 = "151", _("General Lavalle")
    CALLE_152 = "152", _("General Martin Miguel de Guemes")
    CALLE_153 = "153", _("General Paz")
    CALLE_154 = "154", _("General Rodriguez")
    CALLE_155 = "155", _("General Villegas")
    CALLE_156 = "156", _("German Palleros")
    CALLE_157 = "157", _("Goleta Sarandi")
    CALLE_158 = "158", _("Gonzalez Gowland")
    CALLE_159 = "159", _("Graciano Garreador")
    CALLE_160 = "160", _("Guatemala")
    CALLE_161 = "161", _("Guillermo Enrique Hudson")
    CALLE_162 = "162", _("Henderson")
    CALLE_163 = "163", _("Herminio Constanzo")
    CALLE_164 = "164", _("Hilario Ascasubi")
    CALLE_165 = "165", _("Hipolito Bouchard")
    CALLE_166 = "166", _("Hipolito Yrigoyen")
    CALLE_167 = "167", _("Hoerth")
    CALLE_168 = "168", _("I. Madariaga")
    CALLE_169 = "169", _("Independencia")
    CALLE_170 = "170", _("Ingeniero Huergo")
    CALLE_171 = "171", _("Ingeniero Jorge Duclout")
    CALLE_172 = "172", _("Ingeniero Jose Pettis")
    CALLE_173 = "173", _("Intendente Juan Italiani")
    CALLE_174 = "174", _("Isla Aguila")
    CALLE_175 = "175", _("Isla Coronacion")
    CALLE_176 = "176", _("Isla Laurie")
    CALLE_177 = "177", _("Isla Martin Garcia")
    CALLE_178 = "178", _("Isla San Jose")
    CALLE_179 = "179", _("Jewet David")
    CALLE_180 = "180", _("Joaquin Victor Gonzalez")
    CALLE_181 = "181", _("Jorge Miles")
    CALLE_182 = "182", _("Jorge Newbery")
    CALLE_183 = "183", _("Jose Benavidez")
    CALLE_184 = "184", _("Jose Duclout")
    CALLE_185 = "185", _("Jose Hernandez")
    CALLE_186 = "186", _("Jose Manuel Parente")
    CALLE_187 = "187", _("Jose Maria Martinez")
    CALLE_188 = "188", _("Jose Zapiola")
    CALLE_189 = "189", _("Juan Bautista Alberdi")
    CALLE_190 = "190", _("Juan Castro Chavez")
    CALLE_191 = "191", _("Juan Ferrarotti")
    CALLE_192 = "192", _("Juan Garcia Fernandez")
    CALLE_193 = "193", _("Juan Hernandez")
    CALLE_194 = "194", _("Juan Larrea")
    CALLE_195 = "195", _("Juan Queirel")
    CALLE_196 = "196", _("Juan Recarte")
    CALLE_197 = "197", _("Juan XXIII")
    CALLE_198 = "198", _("Juan de Garay")
    CALLE_199 = "199", _("Juana de Arco")
    CALLE_200 = "200", _("Juarez")
    CALLE_201 = "201", _("Junin")
    CALLE_202 = "202", _("La Calandria")
    CALLE_203 = "203", _("La Horqueta")
    CALLE_204 = "204", _("La Pampa")
    CALLE_205 = "205", _("Las Azucenas")
    CALLE_206 = "206", _("Las Calas")
    CALLE_207 = "207", _("Las Dalias")
    CALLE_208 = "208", _("Las Orquideas")
    CALLE_209 = "209", _("Las Rosas")
    CALLE_210 = "210", _("Las Talitas")
    CALLE_211 = "211", _("Las Violetas")
    CALLE_212 = "212", _("Lavalle")
    CALLE_213 = "213", _("Leandro N. Alem")
    CALLE_214 = "214", _("Leopoldo Linan")
    CALLE_215 = "215", _("Libertad")
    CALLE_216 = "216", _("Liniers")
    CALLE_217 = "217", _("Lisandro de La Torre")
    CALLE_218 = "218", _("Lobos")
    CALLE_219 = "219", _("Lola Mora")
    CALLE_220 = "220", _("Los Andes")
    CALLE_221 = "221", _("Los Claveles")
    CALLE_222 = "222", _("Los Glaciares")
    CALLE_223 = "223", _("Los Jazmines")
    CALLE_224 = "224", _("Los Pinos")
    CALLE_225 = "225", _("Los Tulipanes")
    CALLE_226 = "226", _("Luis Guillon")
    CALLE_227 = "227", _("Luis Pasteur")
    CALLE_228 = "228", _("Luis de Sarro")
    CALLE_229 = "229", _("Lujan")
    CALLE_230 = "230", _("Magdalena")
    CALLE_231 = "231", _("Maipu")
    CALLE_232 = "232", _("Mamerto Esquiu")
    CALLE_233 = "233", _("Mannucci")
    CALLE_234 = "234", _("Manuel Belgrano")
    CALLE_235 = "235", _("Manuel Delorenzi")
    CALLE_236 = "236", _("Manuel Jose de Lavarden")
    CALLE_237 = "237", _("Manuel Wieman")
    CALLE_238 = "238", _("Mariano Acosta")
    CALLE_239 = "239", _("Mariano Alegre")
    CALLE_240 = "240", _("Mariano Moreno")
    CALLE_241 = "241", _("Martin Fierro")
    CALLE_242 = "242", _("Maximo Paz")
    CALLE_243 = "243", _("Meliton Legarreta")
    CALLE_244 = "244", _("Mercedes")
    CALLE_245 = "245", _("Miguel Cane")
    CALLE_246 = "246", _("Miguel Fitzgerald")
    CALLE_247 = "247", _("Miguel Garcia Fernandez")
    CALLE_248 = "248", _("Monte Coman")
    CALLE_249 = "249", _("Monte Guarani")
    CALLE_250 = "250", _("Navarro")
    CALLE_251 = "251", _("Neuquen")
    CALLE_252 = "252", _("Nicolas Avellaneda")
    CALLE_253 = "253", _("Nuestras Malvinas")
    CALLE_254 = "254", _("Oceano Atlantico")
    CALLE_255 = "255", _("Olavarria")
    CALLE_256 = "256", _("Olavarria")
    CALLE_257 = "257", _("Olazabal")
    CALLE_258 = "258", _("Omega Petrazzini")
    CALLE_259 = "259", _("Pablo Caceres")
    CALLE_260 = "260", _("Pablo Pizzurno")
    CALLE_261 = "261", _("Parana")
    CALLE_262 = "262", _("Parish Robertson")
    CALLE_263 = "263", _("Patricios")
    CALLE_264 = "264", _("Pavon")
    CALLE_265 = "265", _("Pedro Farina")
    CALLE_266 = "266", _("Pedro Legarte")
    CALLE_267 = "267", _("Pedro Reta")
    CALLE_268 = "268", _("Pehuajo")
    CALLE_269 = "269", _("Pergamino")
    CALLE_270 = "270", _("Pila")
    CALLE_271 = "271", _("Pilar")
    CALLE_272 = "272", _("Plumerillo")
    CALLE_273 = "273", _("Presbitero Orencio Antonio Mainer")
    CALLE_274 = "274", _("Primera Junta")
    CALLE_275 = "275", _("Primo Tricotti")
    CALLE_276 = "276", _("Pringles")
    CALLE_277 = "277", _("Profesor Marxer")
    CALLE_278 = "278", _("Puan")
    CALLE_279 = "279", _("Puan")
    CALLE_280 = "280", _("Puerto Argentino")
    CALLE_281 = "281", _("Puerto Deseado")
    CALLE_282 = "282", _("Puerto Soledad")
    CALLE_283 = "283", _("Pueyrredon")
    CALLE_284 = "284", _("Quiroga")
    CALLE_285 = "285", _("Raimundo Maria Pisani")
    CALLE_286 = "286", _("Ramallo")
    CALLE_287 = "287", _("Ramon Santamarina")
    CALLE_288 = "288", _("Rauch")
    CALLE_289 = "289", _("Raul Mazza")
    CALLE_290 = "290", _("Reconquista")
    CALLE_291 = "291", _("Ricardo Newton")
    CALLE_292 = "292", _("Ricardo Rojas")
    CALLE_293 = "293", _("Rio Gallegos")
    CALLE_294 = "294", _("Rio Grande")
    CALLE_295 = "295", _("Rivadavia")
    CALLE_296 = "296", _("Roberto Petracca")
    CALLE_297 = "297", _("Rosario")
    CALLE_298 = "298", _("Saladillo")
    CALLE_299 = "299", _("Salta")
    CALLE_300 = "300", _("Salto")
    CALLE_301 = "301", _("San Martin")
    CALLE_302 = "302", _("San Pedrito")
    CALLE_303 = "303", _("Santa Fe")
    CALLE_304 = "304", _("Santiago Lumsden")
    CALLE_305 = "305", _("Sastre")
    CALLE_306 = "306", _("Seneca")
    CALLE_307 = "307", _("Senora Teresa Ariz Navarrette de Recarte")
    CALLE_308 = "308", _("Simon Sansinena")
    CALLE_309 = "309", _("Sofia Terrero de Santamarina")
    CALLE_310 = "310", _("T. Ghersi")
    CALLE_311 = "311", _("Talcahuano")
    CALLE_312 = "312", _("Tandil")
    CALLE_313 = "313", _("Teniente Enrique Insua")
    CALLE_314 = "314", _("Teniente Evangelino G. Ford")
    CALLE_315 = "315", _("Teniente Joaquin Castex")
    CALLE_316 = "316", _("Teniente Manuel F. Origone")
    CALLE_317 = "317", _("Teniente Manuel Origone")
    CALLE_318 = "318", _("Tierra del Fuego")
    CALLE_319 = "319", _("Tinogasta")
    CALLE_320 = "320", _("Tomas Alva Edison")
    CALLE_321 = "321", _("Tranque Lauquen")
    CALLE_322 = "322", _("Tres Arroyos")
    CALLE_323 = "323", _("Triunvirato")
    CALLE_324 = "324", _("Ubaldino Ortega")
    CALLE_325 = "325", _("Urquiza")
    CALLE_326 = "326", _("Uruguay")
    CALLE_327 = "327", _("Valentin Alsina")
    CALLE_328 = "328", _("Ventura Avila")
    CALLE_329 = "329", _("Vicente Lopez y Planes")
    CALLE_330 = "330", _("Vicente Ramos")
    CALLE_331 = "331", _("Zarate")