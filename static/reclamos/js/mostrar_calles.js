// Acceder al elemento select de localidad
const LOCALIDAD_SELECT = document.querySelector('#localidad-select');

// Acceder al elemento select de calles
const CALLE_SELECTS = document.querySelectorAll('.calle-select');

// Función para ocultar las opciones de calles que no comiencen con el valor de la localidad seleccionada
function filtrarCalles() {
    // Obtener el valor seleccionado de la localidad
    const LOCALIDAD_SELECCIONADA = LOCALIDAD_SELECT.value;

    // Iterar sobre cada campo de selección de calles
    CALLE_SELECTS.forEach(calleSelect => {
        // Obtener todas las opciones de calles
        const CALLE_OPTION = calleSelect.options;

        // Iterar sobre todas las opciones de calles
        CALLE_OPTION.forEach(option => {
            const CALLE_VALUE = option.value;

            // Verificar si la opción es la opción en blanco
            if (CALLE_VALUE === '') {
                // Mostrar siempre la opción en blanco
                option.style.display = 'block';
            } else if (!CALLE_VALUE.startsWith(LOCALIDAD_SELECCIONADA)) {
                // Ocultar la opción de calle que no cumple el criterio
                option.style.display = 'none';
            } else {
                // Mostrar la opción de calle que cumple el criterio
                option.style.display = 'block';
            }
        });
    });
    // Restablecer la opción seleccionada del select de calles
    CALLE_SELECTS.selectedIndex = 0;
  }

// Agregar el evento de cambio de localidad a todos los campos de selección de calles
CALLE_SELECTS.forEach(calleSelect => {
    calleSelect.addEventListener('change', filtrarCalles);
});

// Llamar a la función para filtrar las calles iniciales al cargar la página
filtrarCalles();


/*const CALLES_DATA = {
    // 9 de Abril
    'R2546787': ['', '28 de Abril', '9 de Abril', '9 de Enero', '9 de Julio', 'A. Paez', 'Aconcagua', 'Alfa Centauro', 'Alfredo Lasalle', 'Aristoteles', 'Atlantida', 'Avenida Doctor Gilberto Elizalde', 'Avenida Luis Vernet', 'Avenida Olimpo', 'Avenida Roberto Oliver', 'Avenida de Mayo', 'Avenida de la Noria', 'Avenida de la Ribera', 'Avenida del Sur', 'Azopardo', 'B. Raffo', 'Belen', 'Biarritz', 'Blanco Encalada', 'Bouchard', 'Bristol', 'Cacique Telomian Condie', 'Camino de la Ribera Sud', 'Carlos Scaglia', 'Castellamare', 'Cerro Catedral', 'Cerro San Javier', 'Cerro Tronador', 'Chapadmalal', 'Colon', 'Colonia Monte Grande', 'Comandante Espora', 'Copacabana', 'Coronel Alvaro Barros', 'Cruz Montiel', 'Cruz del Sur', 'Daniel Defoe', 'Daytona', 'Del Progreso', 'Doctor Ernesto Restelli', 'Domingo Chimondegui', 'Don Segundo Sombra', "Edmundo D'Amicis", 'El Gaucho', 'El Partenon', 'El Resero', 'Emilio Salgari', 'Emilio Zola', 'Esparta', 'Esteban Echeverria', 'Eusebio Rebizo', 'Felix Picquart', 'Fortunato Lopez', 'General Jose Marinzio', 'Remedios de Escalada de San Martin', 'Republica del Peru', 'Ruta de la Tradicion', 'Saenz Valiente', 'San Agustin', 'San Andres', 'San Antonio', 'San Clemente del Tuyu', 'San Fernando', 'San Francisco de California', 'San Joaquin', 'San Juan', 'San Lucas', 'San Nicolas', 'San Pedro', 'San Remo', 'San Sebastian', 'Santa Adela', 'Santa Ana', 'Santa Bernardita', 'Santa Ines', 'Santa Magdalena', 'Santa Margarita', 'Santa Rita', 'Santa Teresita', 'Santiago Lumsden', 'Santos Vega', 'Sargento Mayor Jose Leon Lemos', 'Saturno', 'Sebastian Elcano', 'Sebastian Gaboto', 'Sierra De Velazco', 'Sierra de Ambato', 'Sierra de Fiambala', 'Sierra de Guasaya', 'Sierra de Velazco', 'Simon Sansinena', 'Socrates', 'Sorrento', 'Teniente Enrique Insua', 'Teniente Joaquin Castex', 'Tupungato', 'Urano', 'Valladolid', 'Venus', 'Villa Gesell', 'Vina del Mar', 'Volcan Lanin'],

    // Canning
    'R2546804': ['', 'Agustin Boulan', 'Alejandro Graham Bell', 'Alfredo Sosa', 'Alvarez de Toledo', 'Avenida Mariano Castex', 'Avenida Pedro Dreyer', 'Avenida Sargento Cabral', 'Boulevard Dupuy', 'Boulevard Saint Thomas', 'Chiron', 'Cuba', 'Escribano Francissco Vazquez', 'Fortunato Caceres', 'Gral. Antonio Gonzalez', 'Isidoro Suarez', 'Jose Ignacio De La Rosa', 'Juan Martin de Pueyrredon', 'Juana de Arco', 'Lacarra', 'Lago Argentino', 'Lago Mascardi', 'Libertad', 'M. Vidal', 'Martin Fierro', 'Miguel Angel', 'Neuquen', 'Olavarria', 'Parana', 'Pedro Arocena', 'Pedro Marione', 'Republica de Costa Rica', 'Republica de Cuba', 'Republica de Nicaragua', 'Republica de Panama', 'Rio Limay', 'Ruta Provincial 58', 'Talcahuano', 'Teniente Jose "Pipo" Giribone'],

    // El Jagüel
    'R2546834': ['', '12 de Octubre', '17 de Agosto', '20 de Junio', '25 de Mayo', 'Almafuerte', 'Amado Nervo', 'Andalgala', 'Andres Berasain', 'Angel Rotta', 'Angela Gonzalez de Barbieri', 'Antonio Cervetti', 'Antonio Crespo', 'Antonio Delfino', 'Antonio Terrarosa', 'Arenales', 'Autopista Ezeiza - Canuelas', 'Avenida Dardo Rocha', 'Avenida Jorge Newbery', 'Avenida Julio Argentino Roca', 'Avenida Mariano Castex', 'Avenida Pedro Dreyer', 'Avenida V. Fair', 'Bahia Esperanza', 'Baliza Chiriguano', 'Cabildo', 'Cabo San Antonio', 'Cabo San Jose', 'Camalotes', 'Catamarca', 'Cichero', 'Cornelio Saavedra', 'Costa Rica', 'Dardo Rocha', 'Dean Funes', 'Destacamento Melchor', 'Diagonal Sur', 'Doctor Manuel Julian Medel', 'Domingo Matheu', 'El Aguaribay', 'El Amancay', 'El Boyero', 'El Ceibo', 'El Chaja', 'El Desvio', 'El Irupe', 'El Molino', 'Emilio Trotta', 'Emilio de Laperriere', 'Enrique Santamarina', 'Entre Rios', 'Estancia Los Remedios', 'Evita', 'Faro Patagonia', 'Faro Primero de Mayo', 'Faro Recalada', 'Fernandez Moreno', 'Fernando de Toro', 'Florencio Sanchez', 'Francisco Narciso de Laprida', 'Fray Luis Beltran', 'Fray Mamerto Esquiu', 'General Bartolome Mitre', 'Golfo San Matias', 'Gregorio de La Ferrere', 'Guarani', 'Guido Spano', 'Hipolito Bouchard', 'Isla Decepcion', 'Isla Martin Garcia', 'Isla Trinidad', 'Islas Orcadas del Sur', 'Italiani', 'Joaquin Gonzalez', 'Jorge Newbery', 'Jose Ingenieros', 'Jose Manuel Estrada', 'Jose Marmol', 'Juan Hernandez', 'Juan Miguel Barberena', 'Julio Argentino Roca', 'Justo Santa Maria de Oro', 'La Calandria', 'La Horqueta', 'La Rioja', 'Lanus', 'Las Cina Cinas', 'Leonardo da Vinci', 'Leopoldo Lugones', 'Los Alerces', 'Los Nogales', 'Los Pinos', 'Los Robles', 'Mamerto Esquiu', 'Manuel Cichero', 'Mariano Acosta', 'Marques de Aguado', 'Martin Fierro', 'Maximo Paz', 'Meliton Legarreta', 'Miguel Angel', 'Norberto Lopez', 'Pablo Pizzurno', 'Pedro Gandulfo', 'Pedro Marione', 'Pedro Milano', 'Pedro Palacios', 'Pio XII', 'Presidente Quintana', 'Punta Mogotes', 'Punta Rassa', 'Quiroga', 'Ramon Santamarina', 'Republica de Colombia', 'Republica de Cuba', 'Republica de Nicaragua', 'Republica de Panama', 'Republica de Paraguay', 'Ricardo Guiraldes', 'Ricardo Gutierrez', 'Ricardo Newton', 'Riobamba', 'Risso', 'Rubens', 'San Felipe', 'San Lorenzo', 'San Luis', 'Santa Fe', 'Tilcara', 'Tomas Alva Edison', 'Ugarteche', 'Valentin Alsina', 'Valentina Alsina', 'Vidal', 'Yapeyu'],

    // Luis Guillón
    'R2546803': ['', 'A. Vidal', 'Alf. Varisco', 'Alferez Alberto Sardi', 'Alferez Burlando', 'Alferez Rodrigo Mendiondo', 'Alferez Ruben Bertollo', 'Almafuerte', 'Antonio Dominguez', 'Arquitecto Richard Adams', 'Avenida Facundo Zuviria', 'Avenida Luciano Valette', 'Avenida Nicolas Bruzone', 'Avenida Pedro Suarez', 'Avenida Pedro Suarez (EE) / Capitan de Fragata Moyano (AB)', 'Benjamin Matienzo', 'Bonifacio Gifford', 'Boulevard Buenos Aires', 'Brigadier General Juan Manuel de Rosas', 'Camino de Cintura', 'Canada', 'Capitan Claudio Rosales', 'Celina Grierson', 'Cepeda', 'Chacabuco', 'Chirio', 'Colectora RP4', 'Colonia Monte Grande', 'Cordoba', 'Coronel Alvaro Barros', 'Costa Rica', 'De los Constituyentes', 'Doctor Emilio Cardeza', 'Doctor Rene Favaloro', 'Don Luis Trangoni', 'Dora Catalina Fleitas', 'Eduardo Arana', 'Espana', 'Estevez', 'Estrecho San Carlos', 'Florentino Ameghino', 'Francia', 'Garzon', 'Guatemala', 'Guillermo Dickson', 'Guillermo Wilson', 'H. Fischer', 'Haiti', 'Hilario Ascasubi', 'Hipolito Yrigoyen', 'Honduras', 'Independencia', 'Intendente Celestino Galvan', 'Joaquin Victor Gonzalez', 'Jorge Miles', 'Jorge Newbery', 'Jose Hernandez', 'Jose Madariaga', 'Juan Bautista Alberdi', 'Juan Carlos Wieman', 'Juan Tweedie', 'Juan Varisco', 'Juan de Garay', 'Jujuy', 'Lagos Garcia', 'Las Talitas', 'Lima', 'Liniers', 'Lisandro de La Torre', 'Los Aromos', 'Luis de Sarro', 'Magallanes', 'Manuel Belgrano', 'Maria Esther Balestrini de Lombardi', 'Mariana Arbel', 'Mariano Moreno', 'Martin Coronado', 'Mendoza', 'Miguel Angel', 'Nicaragua', 'Nicolas Avellaneda', 'Nicolas Correa', 'Nueva Escocia', 'Parish Robertson', 'Pavon', 'Pedro Faiat', 'Pedro Zanni', 'Pedro de Rocha', 'Ponce de Leon', 'Primo Tricotti', 'Profesor Marxer', 'Puerto Deseado', 'Rafael de Sanzio', 'Reconquista', 'Republica Argentina', 'Ricardo Rojas', 'Roberto Petracca', 'Rodolfo Pachinotti', 'Rotonda de Llavallol', 'Ruta de la Tradicion', 'San Martin', 'San Nicolas', 'Santa Catalina', 'Sastre', 'Savio', 'Sebastian Maggio', 'Siciliano', 'Subteniente Alfredo Fox', 'Subteniente Antonio Gabaston', 'Subteniente Carlos Fader', 'Subteniente Gamarra', 'Subteniente Urbano Gonzalez', 'Tacuari', 'Tarulli', 'Teniente Evangelino G. Ford', 'Teniente Felix Bourquet', 'Teniente Mario Agustin del Castillo', 'Teniente Martin Retes', 'Teniente O. Larcamon', 'Teniente Primero Alberto Grande', 'Teniente Ruben Ruiz', 'Urbano Gonzalez', 'Urquiza', 'Wilde'],

    // Monte Grande
    'R2546842': ['', '12 de Octubre', '25 de Mayo', '9 de Abril', '9 de Julio', 'Adolfo Alsina', 'Alejo Ortega', 'Alferez Alberto Sardi', 'Alfonsina Storni', 'Alfonso Amat', 'Alfonso Amat (EE) / Avenida Argentina (AB)', 'Almirante Brown', 'Almirante Cordero', 'Alvar Nunez', 'Amado Nervo', 'Anacleto Rojas', 'Andres Berasain', 'Angela Gonzalez de Barbieri', 'Antonio Cervetti', 'Antonio Crespo', 'Antonio Rivero', 'Antonio Terrarosa', 'Arenales', 'Avenida Argentina', 'Avenida Dardo Rocha', 'Avenida Enrique Santamarina', 'Avenida Facundo Zuviria', 'Avenida Fitz Roy', 'Avenida Julio Argentino Roca', 'Avenida Luciano Valette', 'Avenida Luis Vernet', 'Avenida Nicolas Bruzone', 'Avenida Pedro Dreyer', 'Avenida Pedro Suarez', 'Avenida Pedro Suarez (EE) / Capitan de Fragata Moyano (AB)', 'Avenida Roberto Oliver', 'Avenida V. Fair', 'Avila', 'Ayacucho', 'Azcuenaga', 'Azul', 'B. Raffo', 'B. Vidal', 'Bahia Blanca', 'Bahia San Julian', 'Bahia Thetis', 'Balcarce', 'Baliza Chiriguano', 'Barracas', 'Benito Sabato', 'Benjamin Matienzo', 'Bolivar', 'Bolivar', 'Bonifacio Gifford', 'Boulevard Buenos Aires', 'Brigadier Miguel Estanislao de Soler', 'Cabo Corrientes', 'Cabo San Felipe', 'Calle 1', 'Calle 10', 'Calle 11', 'Calle 12', 'Calle 13', 'Calle 14', 'Calle 15', 'Calle 2', 'Calle 3', 'Calle 4', 'Calle 5', 'Calle 7', 'Calle 8', 'Calle 9', 'Calle-', 'Camino de las Latas', 'Capitan Cairo', 'Carlos Pellegrini', 'Carlos Scaglia', 'Carmen de Areco', 'Casacuberta', 'Castelli', 'Catalina Berardi de Battipede', 'Caturini', 'Cepeda', 'Cerro Catedral', 'Chacabuco', 'Chinivasi', 'Cipres', 'Cordoba', 'Cornelio Saavedra', 'Coronel Alvaro Barros', "Coronel D'Elia", 'Coronel Manuel Dorrego', 'Cristobal Colon', 'Daireaux', 'Dean Funes', 'Delfino', 'Dinamarca', 'Doctor Angel Rotta', 'Doctor Emilio Cardeza', 'Doctor Manuel Julian Medel', 'Dolores', 'Dolores Gonzalez Ocantos', 'Domingo Chimondegui', 'Domingo Faustino Sarmiento', 'Don Orione', 'Don Vicente Torro Simo', 'Dona Mayor Humanes de Molina', 'Eduardo Arana', 'El Ceibo', 'El Jacaranda', 'Emilio M. De Laperriere', 'Emilio de Laperriere', 'Enrique Banchs', 'Entre Rios', 'Escobar', 'Escribano R. Di Cio', 'Escribano Rodolfo Di Cio', 'Esquel', 'Estanislao del Campo', 'Esteban Echeverria', 'Esteban Gomez', 'Estrecho San Carlos', 'Eugenio Rebizo', 'Eusebio Rebizo', 'Evaristo Carriego', 'Evita', 'Ezequiel Perez Iglesias', 'F Rodicio', 'Faro Patagonia', 'Faro Primero de Mayo', 'Fernando de Toro', 'Florencio Sanchez', 'Florentino Ameghino', 'Florida', 'Fortunato Caceres', 'Fortunato Lopez', 'Fraga', 'Francisco Garcia Romero', 'Francisco Narciso de Laprida', 'Francisco Recondo', 'Fray Luis Beltran', 'Fregata Heroina', 'French', 'Gabriela Mistral', 'Garzon', 'General Alvarado', 'General Alvear', 'General Bartolome Mitre', 'General Carlos Alvear', 'General Jose Rondeau', 'General Las Heras', 'General Lavalle', 'General Martin Miguel de Guemes', 'General Paz', 'General Rodriguez', 'General Villegas', 'German Palleros', 'Goleta Sarandi', 'Gonzalez Gowland', 'Graciano Garreador', 'Guatemala', 'Guillermo Enrique Hudson', 'Henderson', 'Herminio Constanzo', 'Hilario Ascasubi', 'Hipolito Bouchard', 'Hipolito Yrigoyen', 'Hoerth', 'I. Madariaga', 'Independencia', 'Ingeniero Huergo', 'Ingeniero Jorge Duclout', 'Ingeniero Jose Pettis', 'Intendente Juan Italiani', 'Isla Aguila', 'Isla Coronacion', 'Isla Laurie', 'Isla Martin Garcia', 'Isla San Jose', 'Jewet David', 'Joaquin Victor Gonzalez', 'Jorge Miles', 'Jorge Newbery', 'Jose Benavidez', 'Jose Duclout', 'Jose Hernandez', 'Jose Manuel Parente', 'Jose Maria Martinez', 'Jose Zapiola', 'Juan Bautista Alberdi', 'Juan Castro Chavez', 'Juan Ferrarotti', 'Juan Garcia Fernandez', 'Juan Hernandez', 'Juan Larrea', 'Juan Queirel', 'Juan Recarte', 'Juan XXIII', 'Juan de Garay', 'Juana de Arco', 'Juarez', 'Junin', 'La Calandria', 'La Horqueta', 'La Pampa', 'Las Azucenas', 'Las Calas', 'Las Dalias', 'Las Orquideas', 'Las Rosas', 'Las Talitas', 'Las Violetas', 'Lavalle', 'Leandro N. Alem', 'Leopoldo Linan', 'Libertad', 'Liniers', 'Lisandro de La Torre', 'Lobos', 'Lola Mora', 'Los Andes', 'Los Claveles', 'Los Glaciares', 'Los Jazmines', 'Los Pinos', 'Los Tulipanes', 'Luis Guillon', 'Luis Pasteur', 'Luis de Sarro', 'Lujan', 'Magdalena', 'Maipu', 'Mamerto Esquiu', 'Mannucci', 'Manuel Belgrano', 'Manuel Delorenzi', 'Manuel Jose de Lavarden', 'Manuel Wieman', 'Mariano Acosta', 'Mariano Alegre', 'Mariano Moreno', 'Martin Fierro', 'Maximo Paz', 'Meliton Legarreta', 'Mercedes', 'Miguel Cane', 'Miguel Fitzgerald', 'Miguel Garcia Fernandez', 'Monte Coman', 'Monte Guarani', 'Navarro', 'Neuquen', 'Nicolas Avellaneda', 'Nuestras Malvinas', 'Oceano Atlantico', 'Olavarria', 'Olavarria', 'Olazabal', 'Omega Petrazzini', 'Pablo Caceres', 'Pablo Pizzurno', 'Parana', 'Parish Robertson', 'Patricios', 'Pavon', 'Pedro Farina', 'Pedro Legarte', 'Pedro Reta', 'Pehuajo', 'Pergamino', 'Pila', 'Pilar', 'Plumerillo', 'Presbitero Orencio Antonio Mainer', 'Primera Junta', 'Primo Tricotti', 'Pringles', 'Profesor Marxer', 'Puan', 'Puan', 'Puerto Argentino', 'Puerto Deseado', 'Puerto Soledad', 'Pueyrredon', 'Quiroga', 'Raimundo Maria Pisani', 'Ramallo', 'Ramon Santamarina', 'Rauch', 'Raul Mazza', 'Reconquista', 'Ricardo Newton', 'Ricardo Rojas', 'Rio Gallegos', 'Rio Grande', 'Rivadavia', 'Roberto Petracca', 'Rosario', 'Saladillo', 'Salta', 'Salto', 'San Martin', 'San Pedrito', 'Santa Fe', 'Santiago Lumsden', 'Sastre', 'Seneca', 'Senora Teresa Ariz Navarrette de Recarte', 'Simon Sansinena', 'Sofia Terrero de Santamarina', 'T. Ghersi', 'Talcahuano', 'Tandil', 'Teniente Enrique Insua', 'Teniente Evangelino G. Ford', 'Teniente Joaquin Castex', 'Teniente Manuel F. Origone', 'Teniente Manuel Origone', 'Tierra del Fuego', 'Tinogasta', 'Tomas Alva Edison', 'Tranque Lauquen', 'Tres Arroyos', 'Triunvirato', 'Ubaldino Ortega', 'Urquiza', 'Uruguay', 'Valentin Alsina', 'Ventura Avila', 'Vicente Lopez y Planes', 'Vicente Ramos', 'Zarate'],
};*/

// // Crear un array con los valores de las calles
// let CAMPOS_CALLES = [];
// if (accion == 'actualizar') {
//     CAMPOS_CALLES = [calle0, calle1, calle2];
// };

// // Función para actualizar las opciones del select de calles
// function updateCalleOptions(localidad) {
//     // Iterar sobre cada campo de selección de calles utilizando 'forEach'
//     CALLE_SELECT.forEach(function (calleSelect, index) {
//         // Limpiar las opciones existentes del campo de selección de calles actual
//         calleSelect.innerHTML = '';

//         // Obtener las calles para la localidad seleccionada
//         const CALLES = CALLES_DATA[localidad];

//         if (localidad !== '' && CALLES) {
//             // Agregar las opciones de calles al campo de selección de calles actual
//             CALLES.forEach((calle, indice) => {
//                 const option = document.createElement('option');
//                 option.value = indice;
//                 option.textContent = calle;
//                 // Verificar si el valor de la opción coincide con el valor del campo
//                 if (accion == 'actualizar') {
//                     if (indice == CAMPOS_CALLES[index]) {
//                         option.selected = true; // Establecer como seleccionada la opción correspondiente
//                     }
//                 }
//                 calleSelect.appendChild(option);
//             });
//         }
//     });
// }

// // Función para manejar el evento de cambio en el select de localidad
// function handleLocalidadChange() {
//     const SELECTED_LOCALIDAD = LOCALIDAD_SELECT.value;
//     updateCalleOptions(SELECTED_LOCALIDAD);
// };

// // Agregar un evento de cambio al select de localidad
// LOCALIDAD_SELECT.addEventListener('change', handleLocalidadChange);

// // Obtener el valor preseleccionado en LOCALIDAD_SELECT
// const localidadElegida = LOCALIDAD_SELECT.value;

// // Ejecutar la función updateCalleOptions con la localidad preseleccionada
// updateCalleOptions(localidadElegida);