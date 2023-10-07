let submitBtn= document.querySelector(".suv_submit_btn");


submitBtn.addEventListener("click",()=>{
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
})

