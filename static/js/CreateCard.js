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
  
  var profileImage ='';
  var businessLogo='';
  
  
  user_name.oninput = ChangeUserName; 
  user_position.oninput = ChangeUserPosition; 
  user_number.oninput = ChangeCardPhoneNumber; 
  whatspp_number.oninput = ChangeWhatsappNumber; 
  user_email.oninput = ChangeUserMail ; 
  
  business_name.oninput = ChangeBusinessName; 
  web_url.oninput = ChnageWebUrl; 
  tag_line.oninput = ChangeTagline
  loc_address.oninput = ChangeCardAddress; 

  business_heading.oninput = ChangeBusinessHeading; 
  
  function ChangeBusinessHeading(){
    business_headling_tag.innerText = this.value;
    console.log(this.value)
  }

  function ChangeUserName(){
    card_username.innerText = this.value;
    console.log(this.value)
  }
  
  function ChangeUserPosition(){
    card_position.innerText = this.value;
    // console.log(this.value)
  }
  
  function ChangeBusinessName(){
    card_business_name.innerText = this.value;
    // console.log(this.value)
  }
  
  function ChangeCardPhoneNumber(){
    card_basic_number.innerText = this.value;
    // console.log(this.value)
  }
  
  function ChangeWhatsappNumber(){
    card_whatspp_number.innerText = this.value;
    // console.log(this.value)
  }
  
  function ChangeUserMail(){
    card_user_email.innerText = this.value;
    // console.log(this.value)
  }
  
  function ChnageWebUrl(){
    card_weburl.innerText = this.value;
    // console.log(this.value)
  }
  
  function ChangeTagline(){
    bus_tag_line.innerText = this.value;
    // console.log(this.value)
  }
  
  function ChangeCardAddress(){
    card_address.innerText = this.value;
    // console.log(this.value)
  }
  
  function LogoutUser(){
    const logout_user_url = $('#logout_user_url').val();
    const csrftoken = getCookie('csrftoken');
    $.ajax({
      method: "POST",
      dataType: "json",
      url: logout_user_url,
      data: JSON.stringify({'data':'val'}), 
      processData: false,
      contentType: false,
      mimeType: "multipart/form-data",
      headers: {
        'X-CSRF-TOKEN': csrftoken
      }
    }).done(function( msg ) {
          const pureData =JSON.parse(JSON.stringify(msg));
          const resp = pureData['response'];;
          console.log(pureData)
          // Error Handler : 
      if(resp=='fail'){
          const message = pureData['message'];
          alertify.error(message)
        }
        
        // Success Handler : 
        if(resp=='success'){
          const message = pureData['message'];
          alertify.success(message)
          const auth_url = $('#auth_url').val();
          location.replace(auth_url)
      }
    });
  }





  function ClearCradField(){
    document.getElementById('insta_link').value=''; 
    document.getElementById('twitter_link').value=''; 
    document.getElementById('face_link').value=''; 
    document.getElementById('youtube_link').value=''; 
    document.getElementById('user_name').value=""; 
    document.getElementById('user_position').value=""; 
    document.getElementById('user_number').value=""; 
    document.getElementById('whatspp_number').value=""; 
    document.getElementById('user_email').value=""; 
    document.getElementById('business_name').value=""; 
    document.getElementById('gst_number').value="";
    document.getElementById('stablish_year').value="";
    document.getElementById('web_url').value="";
    document.getElementById('tag_line').value="";
    document.getElementById('business_tag').value="";
    document.getElementById('business_desc').value="";
    document.getElementById('loc_state').value="";
    document.getElementById('loc_city').value="";
    document.getElementById('loc_country').value="";
    document.getElementById('loc_pincode').value="";
    document.getElementById('loc_address').value="";
    document.getElementById('business_heading').value=""; 

  }


  function GetFormsData(){
    const csrftoken = getCookie('csrftoken');
    const my_url =  $('#create_card_handler').val();

    const  userName= document.getElementById('user_name').value; 
    const  business_heading= document.getElementById('business_heading').value; 
    const  position= document.getElementById('user_position').value; 
    const  userNumber= document.getElementById('user_number').value; 
    const  userEmail= document.getElementById('user_email').value; 
    const  userwhatsappNumber= document.getElementById('whatspp_number').value; 
    const  instaLink= document.getElementById('insta_link').value; 
    const  twitterLink= document.getElementById('twitter_link').value; 
    const  faceLink= document.getElementById('face_link').value; 
    const  youtubeLink= document.getElementById('youtube_link').value; 
    const  businessName= document.getElementById('business_name').value; 
    const  gstNumber = document.getElementById('gst_number').value;
    const  stablishedYear = document.getElementById('stablish_year').value;
    const  webUrl = document.getElementById('web_url').value;
    const  tagline = document.getElementById('tag_line').value;
    const  businessTag = document.getElementById('business_tag').value;
    const  businessDesc = document.getElementById('business_desc').value;
    const  state = document.getElementById('loc_state').value;
    const  city = document.getElementById('loc_city').value;
    const  country = document.getElementById('loc_country').value;
    const  pincode = document.getElementById('loc_pincode').value;
    const  address = document.getElementById('loc_address').value;
    


    // console.log(userName)
    // console.log(position)
    // console.log(userNumber)
    // console.log(userwhatsappNumber)
    // console.log(userEmail)
    // console.log(instaLink)
    // console.log(faceLink)
    // console.log(twitterLink)
    // console.log(youtubeLink)
    // console.log(businessName)
    // console.log(gstNumber)
    // console.log(stablishedYear)
    // console.log(webUrl)
    // console.log(tagline)
    // console.log(businessTag)
    // console.log(businessDesc)
    // console.log(state)
    // console.log(city)
    // console.log(country)
    // console.log(pincode)
    // console.log(address)
    // console.log(business_heading)
    // console.log(profileImage)



    var myForm = new FormData();
    myForm.append("profile_image", $("#profile_image")[0].files[0])
    myForm.append("business_logo", $("#business_logo")[0].files[0])
    myForm.append("csrfmiddlewaretoken", $("input[name=csrfmiddlewaretoken]").val())
    myForm.append("userName",  userName)
    myForm.append("position",  position)
    myForm.append("userNumber",  userNumber)
    myForm.append("userwhatsappNumber",  userwhatsappNumber)
    myForm.append("userEmail",  userEmail)
    myForm.append("instaLink",  instaLink)
    myForm.append("faceLink",  faceLink)
    myForm.append("twitterLink",  twitterLink)
    myForm.append("youtubeLink",  youtubeLink)
    myForm.append("businessName",  businessName)
    myForm.append("gstNumber",  gstNumber)
    myForm.append("stablishedYear",  stablishedYear)
    myForm.append("webUrl",  webUrl)
    myForm.append("tagline",  tagline)
    myForm.append("businessTag",  businessTag)
    myForm.append("businessDesc",  businessDesc)
    myForm.append("state",  state)
    myForm.append("city",  city)
    myForm.append("country",  country)
    myForm.append("pincode",  pincode)
    myForm.append("address",  address)
    myForm.append("businessHeading",  business_heading)
     
  $.ajax({
    method: "POST",
    dataType: "json",
    url: my_url,
    data: myForm, 
    processData: false,
    contentType: false,
    mimeType: "multipart/form-data",
    headers: {
      'X-CSRF-TOKEN': csrftoken
    }
  }).done(function( msg ) {
    const card_detail_url = $('#card_detail_url').val();
    const pk=0;
    const pureData =JSON.parse(JSON.stringify(msg));
    const resp = pureData['response'];;    
    console.log(resp)
        // Error Handler : 
    if(resp=='fail'){
        const message = pureData['message'];
        alertify.error(message)
      }
      
      // Success Handler : 
      if(resp=='success'){
        const message = pureData['message'];
        alertify.success(message)
        ClearCradField();
        const pk = pureData['data']; 
        // const detail_url = card_detail_url.replace('1','')+pk;
        // console.log(detail_url)
        // location.replace(detail_url)
    }
  });
}





  let LoadProfile = function(event) {
    let output = document.getElementById('output');
    profileImage = event.target.files[0];
    console.log(profileImage)
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function() {
      URL.revokeObjectURL(output.src) // free memory
    }
  };
  let LoadLogo = function(event) {
    let output = document.getElementById('output-1');
    businessLogo = event.target.files[0];
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function() {
      URL.revokeObjectURL(output.src) // free memory
    }
  };
  
    var cardLogo = document.getElementById('card_logo');
    cardLogo.src = URL.createObjectURL(event.target.files[0]);
    cardLogo.onload = function() {
      URL.revokeObjectURL(cardLogo.src) // free memory
    }