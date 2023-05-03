const $formi = document.getElementById('formi');
const $txtName = document.getElementById('txtName');

(function () {
    $formi.addEventListener('submit', function(e){
        let name = String($txtName.value).trim();
        if(name.length ===0){
            alert("último campo no puede quedar vacío, completalo ok?");
            e.preventDefault();

        }

    });
    
})();