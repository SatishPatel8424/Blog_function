function list_display(){
    var url =  '/blog/blogs/';
    $.ajax({
        type:'GET',
        url: url,
        data : { the_post_list : $('#blogListli').val() },
    success: function(json) {
      $('#blogListli').val('');
    },
    complete: function() {
      setTimeout(list_display, 1000);
    }
  });
}
$(document).ready(function(){
setTimeout(list_display, 5000);
    });