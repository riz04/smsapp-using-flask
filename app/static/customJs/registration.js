
var BASE_URL='http:localhost:8000/'
function registration_click(){
    $.ajax({
        url:`${BASE_URL}/registration`,
        data:JSON.stringify(payload),
        type:'POST',
        success:function(response){
            alert('hello')
        }
    })
}

function create_card_html(item){
return '<div class="card">'+
  
  '<h1>Tailored Jeans</h1>'+
  '<p class="price">$19.99</p>'+
'</div>'
}
$(function() {
    $("form[name='registration']").validate({
      rules: {
        
        name: {
          required: true,
          
        },
        number: {
          required: true,
          
          
        }
      },
       messages: {
        email: "Please enter your name",
       
        password: {
          required: "Please enter Mobile Number",
         
        }
        
      },
      submitHandler: function(form) {
        form.submit();
      }
    });
  });

