
var BASE_URL='http:localhost:8000/'
// function registration_click(){
//     var name=document.getElementById('name').value
//     var number=document.getElementById('number').value
//     var payload={
//         name:name,
//         number:number
//     }
//     $.ajax({
//         url:`${BASE_URL}/registration`,
//         data:JSON.stringify(payload),
//         type:'POST',
//         success:function(response){
//             alert('hello')
//         }
//     })
// }
jQuery.validator.addMethod(
    "regex",
     function(value, element, regexp) {
         if (regexp.constructor != RegExp)
            regexp = new RegExp(regexp);
         else if (regexp.global)
            regexp.lastIndex = 0;
            return this.optional(element) || regexp.test(value);
     },"Wrong Format"
  );
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
        regex:/^[56789]\d{9}$/,
        

          
          
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

