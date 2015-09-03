/**
 * Created by Chelsea on 9/1/15.
 */

var $name=$('[name=name]');
var alert = [];
alert.push('<p>'+ "That email isn't valid. Please try again");
$( "main" ).append(alert);
$( "p" ).hide().css({'text-align': 'center', 'color': '#94BA65'});

function checkIfValid(event) {
    event.preventDefault();
    var inputEmail=$('input[name=email]').val();

        var validInput = /[^@]+@[^@.].+/.test(inputEmail);

        if (!validInput) {
            console.log("I am here!");
            $( "p" ).slideDown(600).show();
            event.preventDefault();
        } else {
            sessionStorage.setItem('name', $name.val());
            console.log($name.val());
            document.location.href = 'http://localhost:63342/tiffany_devCamp/gallery.html';
        }
}

$("#signup").submit(checkIfValid);