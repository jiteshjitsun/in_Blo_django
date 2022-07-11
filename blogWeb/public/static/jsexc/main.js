
console.log("heunik");
function login(){
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let csrf = document.getElementById('csrf').value;

    if(username=='' && password==''){
        alert('Please enter the credentials');
    }

    let data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf,

        },
        'body' : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response);

        if(response.status == 200){
            window.location.href ='/';
        }
        else{
            alert(response.message);
        }
    })

}