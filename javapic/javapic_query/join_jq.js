/**
 * Created by Chelsea on 9/1/15.
 */

var $name=$('[name=name]');

//alert("That is not a valid input. Please try again.");

function checkIfValid(event) {
    event.preventDefault();
    var inputEmail=$('input[name=email]').val();

            var validInput = /[^@]+@[^@.].+/.test(inputEmail);

            if (!validInput) {
                alert("That is not a valid input. Please try again.");
                console.log("I am here!");
                $( 'input' ).css([ "drop-shadow", "0 0 50px" ]);
                event.preventDefault();
                //event.preventDefault(alert("That is not a valid input. Please try again."));
                //invalidInput(event);
            } else {
                sessionStorage.setItem('name', $name.val());
                console.log($name.val());
                document.location.href = 'http://localhost:63342/tiffany_devCamp/gallery.html';
            }
}

//function invalidInput(event) {
//    console.log("Test!");
//    alert("That is not a valid input. Please try again.");
//    event.preventDefault();}

$("#signup").submit(checkIfValid);

//$( 'input' ).css( "drop-shadow", "3px solid red" );