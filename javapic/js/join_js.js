 /**
 * Created by Chelsea on 8/27/15.
 */

var form = document.getElementById("signup");
var inputs = document.getElementsByTagName("input");
var name = document.querySelector('[name=name]');

function checkIfValid(event) {
    event.preventDefault();
    for (var i = 0; i < inputs.length; i++) {
// Looping through the array of inputs
        if (inputs[i].type == 'email') {
            // If while looping it finds a type called 'email'
            var validInput = /[^@]+@[^@.].+/.test(inputs[i].value);
            //Making a var that tests to see if the email is what we want and returns true of false
            if (!validInput) {
                invalidInput(event);
                // If validinput returns a false
                console.log(inputs[i]);
                // Printing for testing
                //calling the function invalidInput
            } else {
                sessionStorage.setItem('name', inputs[0].value);
                //var test = sessionStorage.getItem('test');
                document.location.href = 'http://localhost:63342/tiffany_devCamp/gallery.html'
            }
        }
    }
}




function invalidInput(event) {
    event.preventDefault(alert("That is not a valid input. Please try again."));}

form.addEventListener('submit', checkIfValid, false);