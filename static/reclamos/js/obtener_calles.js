const LOCALIDAD_SELECT = document.querySelector('#localidad-select');
const CALLE_SELECT = document.querySelector('#calle-select');
const CALLE_SELECT1 = document.querySelector('#calle-select1');
const CALLE_SELECT2 = document.querySelector('#calle-select2');

// Agregar un evento de cambio al select de localidad
LOCALIDAD_SELECT.addEventListener('change', () => {
    const selectedLocalidad = LOCALIDAD_SELECT.value;
    console.log(selectedLocalidad)

    // Realizar la solicitud AJAX al servidor
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/calles/?localidad=${selectedLocalidad}`, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // Limpiar las opciones existentes del select de calles
            CALLE_SELECT.innerHTML = '';
            CALLE_SELECT1.innerHTML = '';
            CALLE_SELECT2.innerHTML = '';

            // Obtener la lista de calles del servidor
            const calles = JSON.parse(xhr.responseText);

            // Agregar las opciones de calles al select de calles
            calles.forEach(calle => {
                const option = document.createElement('option');
                option.value = calle.id;
                option.textContent = calle.nombre;
                CALLE_SELECT.appendChild(option);
                CALLE_SELECT1.appendChild(option);
                CALLE_SELECT2.appendChild(option);
            });
        }
    };
    xhr.send();
});
