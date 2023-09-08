

// console.log('Signup page');
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function Signup(){
	const csrftoken = getCookie('csrftoken');
	let url = $('#signup_url').val();
	let username = $('#userUsername').val();
	let passwrod = $('#txtPassword').val();
	let confirmPassword = $('#confirmPassword').val();

	// console.log(username)
	// console.log(passwrod)
	// console.log(confirmPassword)

	if(passwrod!=confirmPassword){
        $('#pass_match').removeClass('password_match_error')  
        $('#pass_match').addClass('password_match_error_active') 
        $('#pass_match').html('password not matched') 
        return;
	}

	if(passwrod==confirmPassword){
        $('#pass_match').addClass('password_match_error')  
		// alertify.success('Ok');
		// console.log('password  matched')
	}

    if(username==null || username == ''){
        $('#pass_match').removeClass('password_match_error')  
        $('#pass_match').addClass('password_match_error_active') 
        $('#pass_match').html('username cant be empty') 
        return;
    }


	$.ajax({
		method: "POST",
		dataType: "json",
		url: url,
		data: JSON.stringify({ 
			"username": username, 
			"password": passwrod ,
		}), 
		headers: {
			'X-CSRF-TOKEN': csrftoken
		}
	}).done(function( msg ) {
        let pureData =JSON.parse(JSON.stringify(msg));
		let resp = pureData['response'];;
        
        console.log(pureData)
        // Error Handler : 
		if(resp=='fail'){
            let message = pureData['message'];
            $('#pass_match').removeClass('password_match_error')  
            $('#pass_match').addClass('password_match_error_active') 
            $('#pass_match').html('username already exist') 
            alertify.error(message)
		}
        
        // Success Handler : 
		if(resp=='success'){
            let create_card_url = $('#create_card').val();
            let pk=0;
			pk = pureData['data']; 
			let create_url = create_card_url.replace('1/','')+pk;
            console.log(create_url)
			// location.replace(create_url)
		}
	});
}

function Login(){
	const csrftoken = getCookie('csrftoken');
	let url = $('#login_url').val();
	let username = $('#loginUsername').val();
	let passwrod = $('#loginPassword').val();


    if(username==null || username == ''){
        $('#login_error_mang').removeClass('login_password_match_error')  
        $('#login_error_mang').addClass('password_match_error_active') 
        $('#login_error_mang').html('username cant be empty') 
    }


	$.ajax({
		method: "POST",
		dataType: "json",
		url: url,
		data: JSON.stringify({ 
			"username": username, 
			"password": passwrod ,
		}), 
		headers: {
			'X-CSRF-TOKEN': csrftoken
		}
	}).done(function( msg ) {
        let pureData =JSON.parse(JSON.stringify(msg));
		let resp = pureData['response'];
        
        // Error Handler : 
		if(resp=='fail'){
            let message = pureData['message'];
            $('#login_error_mang').removeClass('login_password_match_error')  
            $('#login_error_mang').addClass('password_match_error_active') 
            $('#login_error_mang').html(message) 
            alertify.error(message)
		}
        
		// Success Handler : 
		if(resp=='success'){
            let create_card_url = $('#create_card').val();
            let pk=0;
			pk = pureData['data']; 
			let create_url = create_card_url.replace('1/','')+pk;
			location.replace(create_url)
		}
	});
}




$(document).ready(function () {  
    $('#txtPassword').keyup(function () {  
        $('#strengthMessage').html(checkStrength($('#txtPassword').val()))  
    })  
    function checkStrength(password) {  
        var strength = 0  
        if (password.length < 6) {  
            $('#strengthMessage').removeClass()  
            $('#strengthMessage').addClass('Short')  
            return 'Too short'  
        }  
        if (password.length < 1) {  
            $('#strengthMessage').removeClass()    
        }  
        if (password.length > 7) strength += 1  
        // If password contains both lower and uppercase characters, increase strength value.  
        if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)) strength += 1  
        // If it has numbers and characters, increase strength value.  
        if (password.match(/([a-zA-Z])/) && password.match(/([0-9])/)) strength += 1  
        // If it has one special character, increase strength value.  
        if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1  
        // If it has two special characters, increase strength value.  
        if (password.match(/(.*[!,%,&,@,#,$,^,*,?,_,~].*[!,%,&,@,#,$,^,*,?,_,~])/)) strength += 1  
        // Calculated strength value, we can return messages  
        // If value is less than 2  
        if (strength < 2) {  
            $('#strengthMessage').removeClass()  
            $('#strengthMessage').addClass('Weak')  
            return 'Weak'  
        } else if (strength == 2) {  
            $('#strengthMessage').removeClass()  
            $('#strengthMessage').addClass('Good')  
            return 'Good'  
        } else {  
            $('#strengthMessage').removeClass()  
            $('#strengthMessage').addClass('Strong')  
            return 'Strong'  
        }  
    }  
}); 