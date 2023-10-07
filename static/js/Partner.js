

// const submitBtn = document.querySelector(".submit");
const info = document.querySelector(".alert-info");
const error = document.querySelector(".alert-error");
const form= document.querySelector(".form");


function SubmitParnerFome(){
    let name = document.querySelector(".input-1").value;
    let email = document.querySelector(".input-3").value;
    let category = document.querySelector(".input-4").value;
    let website = document.querySelector(".input-5").value;
    let url=document.querySelector(".url-value").value;

    const phoneNumber = phoneInput.getNumber();
    console.log(phoneNumber);
    console.log(url)
    info.style.display = "none";
    error.style.display = "none";
    
    if (phoneInput.isValidNumber()) {
        info.style.display = "";
        info.innerHTML = `Phone number in E.164 format: <strong>${phoneNumber}</strong>`;

        var temp = {
            'name':name, 
            'email':email,
        };
	$.ajax({
		method: "POST",
		content_type:'application/json',
		url: url,
		data:temp,
        cache : false,
        processData: false, 
		// headers: {
		// 	'X-CSRF-TOKEN': csrftoken
		// }
	}).done(function( msg ) {
        let pureData =JSON.parse(JSON.stringify(msg));
		let resp = pureData['response'];;
        
        // console.log(pureData)
        // Error Handler : 
		if(resp=='fail'){
     
            alertify.error(message)
		}
        
        // Success Handler : 
		if(resp=='success'){

		}
	});
    } else {
        error.style.display = "";
        error.innerHTML = `Invalid phone number.`;
    }
};

console.log('Hello');