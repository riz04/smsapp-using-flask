
function registration_click(){
    alert('hello')
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

