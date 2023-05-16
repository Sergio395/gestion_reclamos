const localidadSelect = document.getElementById('localidadSelect');
const calleSelect = document.getElementById('calleSelect');

// Agregar un evento de cambio al select de localidad
localidadSelect.addEventListener('change', () => {
    const selectedLocalidad = localidadSelect.value;

    // Realizar la solicitud AJAX al servidor
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/api/calles/?localidad=${selectedLocalidad}`, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // Limpiar las opciones existentes del select de calles
            calleSelect.innerHTML = '';

            // Obtener la lista de calles del servidor
            const calles = JSON.parse(xhr.responseText);

            // Agregar las opciones de calles al select de calles
            calles.forEach(calle => {
                const option = document.createElement('option');
                option.value = calle.id;
                option.textContent = calle.nombre;
                calleSelect.appendChild(option);
            });
        }
    };
    xhr.send();
});