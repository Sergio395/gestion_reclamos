// Acceder al elemento select de localidad
const LOCALIDAD_SELECT = document.querySelector('#localidad-select');

// Acceder al elemento select de calles
let CALLE_SELECTS = [];

// Función para ocultar las opciones de calles que no comiencen con el valor de la localidad seleccionada
function filtrarCalles() {
    // Obtener el valor seleccionado de la localidad
    const LOCALIDAD_SELECCIONADA = LOCALIDAD_SELECT.value;

    // Iterar sobre cada campo de selección de calles
    CALLE_SELECTS.forEach(calleSelect => {
        // Obtener todas las opciones de calles
        // const CALLE_OPTION = calleSelect.options;
        // Obtener todas las opciones de calles y convertirlo en una matriz
        const CALLE_OPTION = Array.from(calleSelect.options);

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

    // Restablecer la opción seleccionada de los select de calles
    CALLE_SELECTS.forEach(calleSelect => {
        calleSelect.selectedIndex = 0;
    });
}

// Función para inicializar el filtrado de calles
function inicializarFiltradoCalles() {
    // Acceder al elemento select de calles después de que se hayan cargado en el DOM
    CALLE_SELECTS = document.querySelectorAll('.calle-select');

    // Agregar el evento de cambio de localidad a todos los campos de selección de calles
    LOCALIDAD_SELECT.addEventListener('change', filtrarCalles);

    // Llamar a la función para filtrar las calles iniciales
    filtrarCalles();
}

// Llamar a la función para inicializar el filtrado de calles
inicializarFiltradoCalles();