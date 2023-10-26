// import dialogPolyfill from "https://cdn.skypack.dev/dialog-polyfill@0.5.6"

const dialog = document.querySelector("dialog");
const openDialogBtn = document.getElementById("open_dialog");
const closeDialogBtn = document.getElementById("close_dialog");

function openReviewPage(){
    window.open("https://g.page/r/Cf0CyjgaQ-9JEAI/review");
}

function openDialog(){
    xdialog.open({
        title: 'Audit Confirmation',
        body:'\
        <h2 style="color:black">Review our profile, and get:</h2>\
        <p style="color:black; margin-top:30px">\
           Our secret funnel 🚀 that generates  1000+ leads and \
           Premium strategies tailored to your business 📈\
        </p>\
        <p style="color:black">for free to supercharge 😎 your business growth by 10x! 🌟</p>\ '
        ,
        style: 'width:520px; color:"black" ',
        buttons: { ok: 'Review us', cancel: 'Cancel' },
        onok:function(){
            window.open("https://g.page/r/Cf0CyjgaQ-9JEAI/review");
        }
        
    });

}

function openDialog1(){

    const elements = dialog.querySelectorAll(    
  'a, button, input, textarea, select, details, [tabindex]:not([tabindex="-1"])'
    );
    const firstElement = elements[0];
    const lastElement = elements[elements.length - 1];

    const trapFocus = (e) => {
      if (e.key === "Tab") {
        const tabForwards = !e.shiftKey && document.activeElement === lastElement;
        const tabBackwards = e.shiftKey && document.activeElement === firstElement;
        if (tabForwards) {
          // only TAB is pressed, not SHIFT simultaneously
          // Prevent default behavior of keydown on TAB (i.e. focus next element)
          e.preventDefault();
          firstElement.focus();
        } else if (tabBackwards) {
          // TAB and SHIFT are pressed simultaneously
          e.preventDefault();
          lastElement.focus();
        }
      }
    };
    
    const openDialog = () => {
        dialog.showModal();
        dialog.addEventListener("keydown", trapFocus);
    };
    
    const closeDialog = (e) => {
        e.preventDefault();
        dialog.close();
        dialog.removeEventListener("keydown", trapFocus);
        openDialogBtn.focus();
    };

    
    openDialogBtn.addEventListener("click", openDialog);
    closeDialogBtn.addEventListener("click", closeDialog); 

    
    if (typeof dialog.showModal !== "function") {
  /**
   * How to add polyfill outside CodePen conditionally
   * let polyfill = document.createElement("script");
   * polyfill.type = "text/javascript";
   * polyfill.src = "/dist/dialog-polyfill.js";
   * document.body.append(polyfill);
  
   * const polyfillStyles = document.createElement("link");
   * polyfillStyles.rel = "stylesheet";
   * polyfillStyles.href = "dialog-polyfill.css";
   * document.head.append(polyfillStyles);
   **/

  // Register polyfill on dialog element once the script has loaded
       dialogPolyfill.registerDialog(dialog);
    }
}

function surveySubmit(){
    let url=document.querySelector('.url-value').value;
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    let email=document.getElementById('suv_email').value;
    console.log(email);

    if(validRegex.test(email)){
        let yes_1= document.getElementById('yes-1').checked;
        let no_1= document.getElementById('no-1').checked;
    
        let yes_2= document.getElementById('yes-2').checked;
        let no_2= document.getElementById('no-2').checked;
    
        let yes_3= document.getElementById('yes-3').checked;
        let no_3= document.getElementById('no-3').checked;
    
        let yes_4= document.getElementById('yes-4').checked;
        let no_4= document.getElementById('no-4').checked;
        
        let yes_5= document.getElementById('yes-5').checked;
        let no_5= document.getElementById('no-5').checked;
    
        let yes_6= document.getElementById('yes-6').checked;
        let no_6= document.getElementById('no-6').checked;
    
        let yes_7= document.getElementById('yes-7').checked;
        let no_7= document.getElementById('no-7').checked;
    
        let yes_8= document.getElementById('yes-8').checked;
        let no_8= document.getElementById('no-8').checked;
    
        let yes_9= document.getElementById('yes-9').checked;
        let no_9= document.getElementById('no-9').checked;
    
        let yes_10= document.getElementById('yes-10').checked;
        let no_10= document.getElementById('no-10').checked;
    
        let yes_11= document.getElementById('yes-11').checked;
        let no_11= document.getElementById('no-11').checked;
    
        let yes_12= document.getElementById('yes-12').checked;
        let no_12= document.getElementById('no-12').checked;
    
        let yes_13= document.getElementById('yes-13').checked;
        let no_13= document.getElementById('no-13').checked;
    
        let yes_14= document.getElementById('yes-14').checked;
        let no_14= document.getElementById('no-14').checked;
    
        let yes_15= document.getElementById('yes-15').checked;
        let no_15= document.getElementById('no-15').checked;
    
        let yes_16= document.getElementById('yes-16').checked;
        let no_16= document.getElementById('no-16').checked;
    
        console.log(yes_1);
    
    
        $.ajax({
            method: "POST",
            content_type:'application/json',
            url: url,
            data: JSON.stringify({
                'email':email,
    
                'yes_1':yes_1,
                'no_1':no_1,
    
                'yes_2':yes_2,
                'no_2':no_2,
    
                'yes_3':yes_3,
                'no_3':no_3,
    
                'yes_4':yes_4,
                'no_4':no_4,
    
                'yes_5':yes_5,
                'no_5':no_5,
    
                'yes_6':yes_6,
                'no_6':no_6,
    
                'yes_7':yes_7,
                'no_7':no_7,
    
                'yes_8':yes_8,
                'no_8':no_8,
    
                'yes_9':yes_9,
                'no_9':no_9,
    
                'yes_10':yes_10,
                'no_10':no_10,
    
                'yes_11':yes_11,
                'no_11':no_11,
    
                'yes_12':yes_12,
                'no_12':no_12,
    
                'yes_13':yes_13,
                'no_13':no_13,
    
                'yes_14':yes_14,
                'no_14':no_14,
    
                'yes_15':yes_15,
                'no_15':no_15,
    
                'yes_16':yes_16,
                'no_16':no_16,
                
            }),
    
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
                openDialog1();
            }
        });
    }else{
        alert('please fill right Email Id');
    }
}





