
function newsEmailRegister(){
    const email=document.querySelector(".add-email").value;
    const url= document.querySelector(".newsletter-url").value;
    console.log(url);

    $.ajax({
        method: "POST",
        content_type: "application/json",
        url: url,
        data: JSON.stringify(
            { "email": email}
        )
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
}