

// const submitBtn = document.querySelector(".submit");
const info = document.querySelector(".alert-info");
const error = document.querySelector(".alert-error");


function SubmitParnerFome(){
    info.style.display = "none";
    error.style.display = "none";

    let name = document.querySelector(".input-1").value;
    let email = document.querySelector(".input-3").value;
    let category = document.querySelector(".input-4").value;
    let website = document.querySelector(".input-5").value;
    let url=document.querySelector(".url-value").value;
    let phoneNumber = phoneInput.getNumber();
    
    // console.log(phoneNumber);
    // console.log(url)
    // console.log(name)
    // console.log(email)
    // console.log(category)
    // console.log(website)


    
    if (phoneInput.isValidNumber()) {
        info.style.display = "";
        info.innerHTML = `Phone number in E.164 format: <strong>${phoneNumber}</strong>`;


	$.ajax({
		method: "POST",
		content_type:'application/json',
		url: url,
		data: JSON.stringify({
            'name':name, 
            'email':email,
            'catigory':category, 
            'phone':phoneNumber, 
            'website':website, 
    
        }),
		// headers: {
		// 	'X-CSRF-TOKEN': csrftoken
		// }
	}).done(function( msg ) {
        let pureData =JSON.parse(JSON.stringify(msg));
        console.log(pureData);
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

console.log('parner page working')