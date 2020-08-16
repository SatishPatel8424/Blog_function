function closures() {
  var a = 4;

  $('#closer_demo').click(function (){
      $('#demo_display').html('<h4> '+ a*a +'</h4>');
  });
}
