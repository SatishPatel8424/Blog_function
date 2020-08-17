$(document).ready(function () {
    var element;
    var container;
    var index;
    var $dialog;
    var g;
    var worker;
    var person;
    var jsonData;

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
    element = $('#target');
    container = $('#container');
    index = container.children().index(element);
    $('#display').text('index is :'+index);
    // page x and y display
    $("#click_element").click(function(event){
        output = 'user clicked on : ' + event.pageX + '/' + event.pageY;
          $('#display_elements').text(output);
    });

    $('input[type="text"]').focus(function (){
        $(this).next('span.help').removeAttr('hidden');
    }).blur(function (){
        $('span.help').attr('hidden','hidden');
    });


    $('form').on('click','button.validate',function (){
        $('#button-validate').text("clicked");
    });

    $('#createButton').click(function (){
        $('#div_Target').html('<button type="Button" class="btn-primary updater">New Button</button>');
    });
    $('#button_forms').delegate('button.updater','click',function (){
        $('#Button_display_new').text($(this).text() + ' was clicked!');
    });

    // wrap example
    $('#wrap-target').click(function (){
        $('.wrap-me').wrap('<div style="color: red"></div>');
    });
    // replacewith example
    $('#executer').click(function (){
        $('#newContent').replaceWith('<div style="color: red"> content replace with new content</div>');
    });
    // clone example
    $dialog = $('#dialog').clone();
    $dialog.removeAttr('id');
    $('#executer-clone').click(function (){
        $('#container-clone').append($dialog.clone());
    });
    sayHiBye("satish","patel");
    closures();
    // worker demo
    worker = new Worker('./js/worker.js');
    worker.addEventListener('message',function (e){
       if(e.data === "READY"){
           $('#messages').append('<li> worker ready </li>');
           $('#send-message').removeAttr('disabled').click(function (){
               var message = $('#message').val();
                worker.postMessage(message);
           });
           $('#message').focus();
       }else {
           $('#messages').append('<li>'+ e.data + '</li>');
           $('#message').val('').focus();
       }
    });
    //Serializing an object
    $('#stringify').click(function (){
        person = new Object();
        person.firstName = $('#first-name').val();
        person.lastName = $('#last-name').val();

        jsonData = JSON.stringify(person);
        $('#json-data').val(jsonData);
    });
    $('#parse').click(function (){
        jsonData = $('#json-data').val();

        person = JSON.parse(jsonData);
        $('#first-name').val(person.firstName);
        $('#last-name').val(person.lastName);
    });
    $('#getdata').click(function (){
        $.get('/js/',function (data){
            $('#GetOutput').text(data);
        });

    });

    $('#load_data_id').click(function (){
       person = { firstName1: $('#first-name1').val(),
           lastName1: $('#last-name1').val()};
       $.post('/js/',person).done(function (data){
        $('#formoutput').text(data.firstName1 + ' ' + data.lastName1);
       });

    });


});
















