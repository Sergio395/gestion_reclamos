const $formi = document.getElementById('formi');
const $txtName = document.getElementById('txtName');

(function () {
    $formi.addEventListener('submit', function(e){
        let name = String($txtName.value).trim();
        if(name.length ===0){
            alert("N° de cuadrícula, este campo no puede quedar vacío, completalo por favor");
            e.preventDefault();

        }

    });
    
})();