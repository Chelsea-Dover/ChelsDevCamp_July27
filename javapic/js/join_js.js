 /**
 * Created by Chelsea on 8/27/15.
 */
//var signupInfo = document.getElementById('signup')
//
//function vailEmail(el){
//    var checkFor = /[^@]+@[^@]+/.test(el.value);
//    if (valid) {
//
//        console.log('signup')
//    }
//    return valid;
//}
//var signupInfo = document.getElementById('signup');
//
//function checkifValidEmail(email) {
//
//    for (var i=0; i < signupInfo.length; i++) {
//        var re = /\S+@\S+\.\S+/;
//        return re.test(email);
//    }
//}
function validateRequired(el) {
     if ( isRequired(el)) {
         var valid = !isEmpty(el);
         if (!valid) {
             setErrorMessage(el, 'Field is required');
         }
         return valid;
     }
     return true
 }


(function () {
    document.forms.register.noValidate = true;
    ('form').on('submit', function(e) {
        var elements = this.elements;
        var valid = {};
        var isValid;
        var isFormValid;

        for (var i=0; i < elements.length; i++) {

            isValid = validateRequired(elements[i]) && validateTypes(elements[i]);
            if (!isValid) {
                showErrorMessage(elements[i]);
            } else {
                removeErrorMessage(elements[i]);
            }
            valid[elements[i].id] = isValid;
        }

        for (var field in valid) {
            if (!valid[field]) {
                isFormValid = false;
                break;

            }
            isFormValid = false
        }
        if (!isFormValid) {
            e.preventDefault();
        }
    })
});