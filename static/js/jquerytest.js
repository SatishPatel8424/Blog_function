$(document).ready(function () {
    $("button").click(function () {
        $("p").hide();
    });

    // h1 tage is click to hide
    $("h1").click(function(){
    $(this).hide();
  });

    // mouse entered time working
    $("#h2").mouseenter(function(event){
        alert("You entered p1!");
        event.preventDefault();
    });

    // mouse leave methods
     $("#h3").mouseleave(function (event){
        alert("mouse is leave");
        event.preventDefault();
    });

     // input type to focus and blur
     $("input").focus(function (){
        $(this).css("background-color", "yellow");
    });
    $("input").blur(function (){
        $(this).css("background-color", "green");
    });
    // hide and show using button
     $("#hidebutton").click(function ()
    {
        $("h5").hide(1000);
    });
    $("#showbutton").click(function ()
    {
        $("h5").show(2000);
    });

    //fadeIn example
    $("#btnfade").click(function (){
        $("#div1").fadeIn("slow");
        $("#div2").fadeIn(2000);
        $("#div3").fadeIn(5000);

    });
    //fadeout example
     $("#buttonout").click(function(){
        $("#div4").fadeOut();
        $("#div5").fadeOut("slow");
        $("#div6").fadeOut(3000);
  });
     // fade toggle example
    $("#buttonToggle").click(function(){
        $("#box1").fadeToggle();
        $("#box2").fadeToggle("slow");
        $("#box3").fadeToggle(3000);
  });
    $("#buttonTo").click(function(){
        $("#box4").fadeTo("fast",0.15);
        $("#box5").fadeTo("slow",0.5);
        $("#box6").fadeTo(3000,0.8);

  });
    var element = $('#target');
    var container = $('#container');
    var index = container.children().index(element);
    $('#display').text('index is :'+index);
    // page x and y display
    $("#click_element").click(function(event){
        output = 'user clicked on : ' + event.pageX + '/' + event.pageY;
          $('#display_elements').text(output);

      });
    $(function (){
       $('input[type="text"]').focus(function (){
           $(this).next('span.help').removeAttr('hidden');
        }).blur(function (){
            $('span.help').attr('hidden','hidden');
       });
     });





});
















