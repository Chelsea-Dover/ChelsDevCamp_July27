/**
 * Created by Chelsea on 8/27/15.
 */
setInterval(function(){ changebg(); }, 20000);

var bgImg = document.getElementById("jumbotron");
//console.log(bgImg.bgImg.style.backgroundImage = "image");
var i = 1;
//var testImg = "images/pdxcg_0" + i + ".jpg";

function changebg() {
    if (i<=9){
        console.log(i);
        bgImg.style.backgroundImage = "url('images/pdxcg_0" + i + ".jpg')";
    }
    else {
        bgImg.style.backgroundImage = "url('images/pdxcg_" + i + ".jpg')";
        console.log(i);
    }
    console.log(i);
    if (i===60) {
        i=0;
    }
    i++;
    //testImg = "images/pdxcg_0" + i + ".jpg";
    console.log(bgImg.style.backgroundImage);
}