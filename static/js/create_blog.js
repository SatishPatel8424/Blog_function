$(document).ready(function(){
    $("#CreateFormid").submit(function(event){
        event.preventDefault();
        var serializedData = $(this).serialize();

        $.ajax({
            type : 'POST',
            url :  "/blog/create-blog/",
            data : serializedData,

            success : function(response){
                console.log(response);
                console.log("successful");
                $('.alert').alert()
                $('#message').text("Post saved successfully");


            },
            error : function(response){
                console.log(response);
                console.log("Error");
                 $('.alert').alert()
                $('#message').text("Post saved successfully");
            }
      	});
        return false;
   });


});