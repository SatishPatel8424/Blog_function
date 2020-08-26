$(document).ready(function(){
    $("#id_username").change(function () {
      var form = $(this).closest("form");

      var serializedData = $(this).serialize();
      $.ajax({
        type : 'POST',
        url: '/ajax/validate_username',
        data: serializedData,
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
            alert(data.error_message);
          }
        }
      });

    });
});