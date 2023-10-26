let services=[];

function queryExtractor(el){
  if (services.includes(el.innerText)) {
    el.classList.remove('activate');
    services.pop(el.innerText);
  }else{
    el.classList.add('activate');
    services.push(el.innerText);
  }
}

function querySubmit(){
  const url= document.querySelector(".query-url").value;
  const name= document.querySelector(".query-name").value;
  const phone= document.querySelector(".query-email").value;
  const email= document.querySelector(".query-email").value;
  const message= document.querySelector(".query-message").value;
  const queryImg= document.querySelector(".query-form-img");
  console.log(message);
  
  $.ajax({
    method:"POST",
    content_type:"application/js",
    url:url,
    data:JSON.stringify({
      'name':name, 
      'phone':phone, 
      'email':email,
      'services':services,
      'message':message
    })
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
        queryImg.src="static/img/green_tick.png";
        let modalHeading=document.querySelector(".modal-title").textContent="Congrats for joining the journey towards 1%";
      }
    });
}








$(document).ready(function(){
  $('.customer-logos').slick({
    slidesToShow: 6,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1000,
    arrows: false,
    dots: false,
    pauseOnHover: false,
    responsive: [{
      breakpoint: 768,
      settings: {
        slidesToShow: 4
      }
    }, {
      breakpoint: 520,
      settings: {
        slidesToShow: 3
      }
    }]
  });
});

document.querySelector('.submit-email').addEventListener('mousedown', (e) => {
  e.preventDefault();
  document.querySelector('.subscription').classList.add('done');
});

