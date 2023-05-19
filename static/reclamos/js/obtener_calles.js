const LOCALIDAD_SELECT = document.querySelector('#localidad-select');
const CALLE_SELECT = document.querySelectorAll('.calle-select');

// Agregar un evento de cambio al select de localidad
LOCALIDAD_SELECT.addEventListener('change', () => {
    const selectedLocalidad = LOCALIDAD_SELECT.value;

    // Realizar la solicitud AJAX al servidor
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/calles/?localidad=${selectedLocalidad}`, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // Limpiar las opciones existentes del select de calles
            CALLE_SELECT.innerHTML = ''; //!FOR PARA ITERAR LISTA DE CAMPOS CALLE_SELECT

            // Obtener la lista de calles del servidor
            const calles = JSON.parse(xhr.responseText);

            // Agregar las opciones de calles al select de calles
            calles.forEach(calle => {
                const option = document.createElement('option');
                option.value = calle.id;
                option.textContent = calle.nombre;
                CALLE_SELECT.appendChild(option);
            });
        }
    };
    xhr.send();
});
