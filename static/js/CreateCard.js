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
  
    // var cardLogo = document.getElementById('card_logo');
    // cardLogo.src = URL.createObjectURL(event.target.files[0]);
    // cardLogo.onload = function() {
    //   URL.revokeObjectURL(cardLogo.src) // free memory
    // }

    // const indianStates = {
    //   AndamanAndNicobarIslands: ["Port Blair", "Diglipur", "Mayabunder", "Rangat", "Ferrargunj", "Havelock Island", "Neil Island", "Little Andaman", "Car Nicobar", "Campbell Bay", "Great Nicobar", "Long Island", "Baratang Island", "Wandoor", "Kalighat", "Bombooflat", "Garacharma", "Kadamtala", "Kamorta", "Katchal", "Nancowry", "Nicobar", "Port Blair", "Rangat", "Shaheed Dweep", "Smith Island", "Teressa Island"],
    //   AndhraPradesh: ["Visakhapatnam", "Vijayawada", "Guntur", "Nellore", "Kurnool", "Rajahmundry", "Kakinada", "Tirupati", "Anantapur", "Kadapa", "Vizianagaram", "Eluru", "Ongole", "Nandyal", "Machilipatnam", "Adoni", "Tenali", "Proddatur", "Chittoor", "Hindupur", "Bhimavaram", "Madanapalle", "Guntakal", "Dharmavaram", "Gudivada", "Srikakulam", "Narasaraopet", "Tadipatri", "Tadepalligudem", "Chilakaluripet", "Yemmiganur", "Kadiri", "Anakapalle", "Kavali", "Palasa-Kasibugga", "Sullurpeta", "Tanuku", "Rayachoti", "Srikalahasti", "Bapatla", "Naidupet", "Nagari", "Gudur", "Vinukonda", "Narasapuram", "Nuzvid", "Markapur", "Ponnur", "Repalle", "Ramachandrapuram", "Pedana", "Pithapuram", "Punganur", "Kandukur", "Amalapuram", "Venkatagiri", "Nandyal", "Mandapeta", "Giddalur", "Venkatagiri", "Nandyal", "Mandapeta", "Giddalur", "Venkatagiri", "Nandyal", "Mandapeta", "Giddalur"],
    //   ArunachalPradesh: ["Itanagar", "Naharlagun", "Pasighat", "Roing", "Tezu", "Ziro", "Aalo", "Bomdila", "Changlang", "Daporijo", "Khonsa", "Seppa", "Tawang", "Yingkiong", "Bordumsa", "Deomali", "Dirang", "Hayuliang", "Mechuka", "Miao", "Namsai", "Namtok", "Nirjuli", "Pangin", "Rupa", "Sagalee", "Tuting", "Vijoynagar", "Wakro", "Yachuli"],
    //   Assam: ["Guwahati", "Silchar", "Dibrugarh", "Jorhat", "Nagaon", "Tinsukia", "Tezpur", "Karimganj", "Hailakandi", "Sivasagar", "Goalpara", "Dhubri", "Diphu", "North Lakhimpur", "Bongaigaon", "Barpeta", "Nalbari", "Mangaldoi", "Dhemaji", "Lanka", "Morigaon", "Nagaon", "Sibsagar", "Sonari", "Tinsukia", "Duliajan", "Digboi", "Margherita", "Namrup", "Nazira", "Sadiya", "Bokajan", "Dergaon", "Golaghat", "Jorhat", "Mariani", "Majuli", "Titabor", "Amguri", "Bihpuria", "Gohpur", "Rangapara", "Tezpur", "Udalguri", "Biswanath Chariali", "Dhekiajuli", "Kalaigaon", "Mangaldoi", "Tangla", "Barama", "Barpeta Road", "Pathsala", "Sarthebari", "Abhayapuri", "Bijni", "Chapar", "Dhubri", "Gauripur", "Mankachar", "South Salmara", "Bokakhat", "Dergaon", "Golaghat", "Numaligarh", "Sarupathar", "Bilasipara", "Chapar", "Gauripur", "Gossaigaon", "Kokrajhar", "Kokrajhar", "Bijni", "Bilasipara", "Gossaigaon", "Kokrajhar", "Kokrajhar", "Bijni", "Bilasipara", "Gossaigaon", "Kokrajhar"],
    //   Bihar: ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Darbhanga", "Arrah", "Bihar Sharif","Motihari", "Saharsa", "Hajipur", "Bettiah", "Sasaram", "Dehri", "Siwan", "Motipur", "Nawada", "Bagaha", "Buxar", "Kishanganj", ... "Jamui", "Sitamarhi", "Jehanabad", "Aurangabad", "Lakhisarai", "Narkatiaganj", "Sheikhpura", "Barh", "Fatwah", "Madhubani", "Samastipur", "Mokama", "Supaul", "Dumraon", "Araria", "Forbesganj", "Bhabua", "Nokha", "Rafiganj", "Munger", "Sultanganj", "Murliganj", ... "Sheohar", "Baruni", "Sherghati", "Marhaura", "Warisaliganj", "Revelganj", "Maner", "Mahnar Bazar", "Piro", "Bikramganj", "Jamalpur", ... "Kasba", "Rajgir", "Sonepur", "Amarpur", "Mokameh", "Belsand", "Raxaul Bazar", "Bihariganj", "Lalganj", "Hisua", "Bariarpur","Rajauli", "Islampur", "Ghoghardiha", "Jagdispur", "Koath", "Sikandra", "Jamui", "Bihar Sharif", "Buxar", "Dehri", "Hajipur","Motihari", "Muzaffarpur", "Patna", "Purnia", "Saharsa", "Samastipur", "Sasaram", "Sitamarhi", "Siwan", "Supaul", "Chhapra", "Gopalganj", "Katihar", "Madhubani", "Nalanda", "Vaishali", "West Champaran", "East Champaran", "Begusarai", "Bhojpur", "Buxar", "Darbhanga", "Gaya", "Gopalganj", "Jamui", "Jehanabad", "Kaimur", "Katihar", "Khagaria", "Kishanganj", "Lakhisarai", "Madhepura","Madhubani", "Munger", "Muzaffarpur", "Nalanda", "Nawada", "Patna", "Purnia", "Rohtas", "Saharsa", "Samastipur", "Saran","Sheikhpura", "Sheohar", "Sitamarhi", "Siwan", "Supaul", "Vaishali"],
    //   Chandigarh: ["Chandigarh"],
    //   Chhattisgarh: ["Raipur", "Bhilai", "Bilaspur", "Korba"],
    //   DadraAndNagarHaveliAndDamanAndDiu: ["Silvassa", "Daman", "Diu"],
    //   Delhi: ["New Delhi", "Noida", "Gurgaon", "Faridabad"],
    //   Goa: ["Panaji", "Vasco da Gama", "Margao", "Mapusa"],
    //   Gujarat: ["Ahmedabad", "Surat", "Vadodara", "Rajkot"],
    //   Haryana: ["Chandigarh", "Faridabad", "Gurgaon", "Hisar"],
    //   HimachalPradesh: ["Shimla", "Mandi", "Solan", "Dharamshala"],
    //   JammuAndKashmir: ["Srinagar", "Jammu", "Anantnag", "Baramulla"],
    //   Jharkhand: ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro"],
    //   Karnataka: ["Bangalore", "Mysore", "Hubli", "Mangalore"],
    //   Kerala: ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur"],
    //   Lakshadweep: ["Kavaratti"],
    //   MadhyaPradesh: ["Bhopal", "Indore", "Jabalpur", "Gwalior"],
    //   Maharashtra: ["Mumbai", "Pune", "Nagpur", "Nashik"],
    //   Manipur: ["Imphal", "Thoubal", "Bishnupur", "Churachandpur"],
    //   Meghalaya: ["Shillong", "Tura", "Nongpoh", "Jowai"],
    //   Mizoram: ["Aizawl", "Lunglei", "Saiha", "Champhai"],
    //   Nagaland: ["Kohima", "Dimapur", "Mokokchung", "Tuensang"],
    //   Odisha: ["Bhubaneswar", "Cuttack", "Rourkela", "Berhampur"],
    //   Puducherry: ["Puducherry", "Karaikal", "Mahe", "Yanam"],
    //   Punjab: ["Ludhiana", "Amritsar", "Jalandhar", "Patiala"],
    //   Rajasthan: ["Jaipur", "Jodhpur", "Udaipur", "Ajmer"],
    //   Sikkim: ["Gangtok", "Namchi", "Gyalshing", "Rangpo"],
    //   TamilNadu: ["Chennai", "Coimbatore", "Madurai", "Salem"],
    //   Telangana: ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar"],
    //   Tripura: ["Agartala", "Udaipur", "Dharmanagar", "Kailasahar"],
    //   UttarPradesh: ["Lucknow", "Kanpur", "Agra", "Varanasi"],
    //   Uttarakhand: ["Dehradun", "Haridwar", "Roorkee", "Haldwani"],
    //   WestBengal: ["Kolkata", "Howrah", "Durgapur", "Asansol"]
    // };
// const stateSel=document.getElementById("state");
// const citySel=document.getElementById("cities");
// function printState(){
//   for (const i of Object.keys(indianStates)) {
//     const option=document.createElement('option');
//     option.value=i;
//     option.text=i;
//     stateSel.appendChild(option);
//   }
// }
// printState();

// function printCity(){
//   console.log(stateSel.value);
//   citySel.innerHTML = "";
//   indianStates[stateSel.value].forEach(element => {
//     const option=document.createElement('option');
//     option.value=element;
//     option.text=element;
//     citySel.appendChild(option);
//   });
// }

var checkList = document.getElementById('list1');
checkList.getElementsByClassName('anchor')[0].onclick = function(evt) {
  if (checkList.classList.contains('visible'))
    checkList.classList.remove('visible');
  else
    checkList.classList.add('visible');
}
const ownerInfo=document.querySelector(".owner-info");
const businessInfo=document.querySelector(".buss-info");
const socialInfo=document.querySelector(".social-info");

function form1Hide(){
  ownerInfo.classList.add("hide-display");
  businessInfo.classList.remove("hide-display");
}

function form2Hide(){
  businessInfo.classList.add("hide-display");
  socialInfo.classList.remove("hide-display");
}

