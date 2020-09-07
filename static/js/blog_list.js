$(document).ready(function(){

    setInterval(function(){
        let url =  '/blog/blogs/';
        $.ajax({
            type:'GET',
            url: url,

            success: function(response) {
                $("#BlogList_ajax").html('');

                $.each(JSON.parse(response),function(i,v)
                {
                    $('#BlogList_ajax').append('<li> <a href="">'+v.fields.name+'</a></li>');
                })
            },
            error: function (response) {
                console.log(response)
            }
        });
    }, 25000)

});
