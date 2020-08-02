$(document).ready(function () {
    $("button").click(function () {
        $("p").hide();
    });
});
$(document).ready(function(){
  $("h1").click(function(){
    $(this).hide();
  });
});
$(document).ready(function (){
   $("#h2").mouseenter(function(){
        alert("You entered p1!");
    });
});
$(document).ready(function (){
    $("#h3").mouseleave(function (){
        alert("mouse is leave");
    });
});
$(document).ready(function (){
    $("input").focus(function (){
        $(this).css("background-color", "yellow");
    });
    $("input").blur(function (){
        $(this).css("background-color", "green");
    });
});
$(document).ready(function (){
    $("#hidebutton").click(function ()
    {
        $("h5").hide();
    });
    $("#showbutton").click(function ()
    {
        $("h5").show();
    });
});
