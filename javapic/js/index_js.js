/**
 * Created by Chelsea on 8/27/15.
 */
//Makes the Jumbo-tron run through an amount of the photos from the file images
//var jumboPictures = document.getElementById('jumbotron')
//var file2 ="images/pdxcg*.jpg";
//setInterval(function(){ alert("Test!"); }, 20000);
//loop (function() {
//        if jumboPictures[]
//    }
//)
//
//for (var i=0; i < jumboPictures.length; i++)


//var timer = setTimeOut(newImage, 200000);
//function makeAlt() {
//    var images = document.getElementsByTagName('img');
//    var numImages = images.length;
//    for (i = 0; i < numImages; i++) {
//        images[i].alt = images[i].src;
//        images[i].title = images[i].src;
//    }
//}
setInterval(function(){ changebg(); }, 2000);

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