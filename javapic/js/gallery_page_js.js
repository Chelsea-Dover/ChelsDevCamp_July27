/**
 * Created by Chelsea on 8/27/15.
 */


var position = document.getElementById("gallery");
var displayImage = document.getElementById("image_show");
var imageChild = displayImage.children[0];

var images = [];
function arrayOfImages() {
    for (var i=1; i<=60; i ++) {
        if (i<=9){
            images.push("images/pdxcg_0" + i + ".jpg");

        } else {
            images.push("images/pdxcg_" + i + ".jpg");
        }
    }
    //console.log(images);
}

arrayOfImages();

for (var i=0; i<images.length; i++) {

        var li = document.createElement("li");
        var img = document.createElement("img");
        img.src = images[i];

        li.appendChild(img);
        position.appendChild(li);
}

position.addEventListener('click',function() {displayLargeImage(event); });
displayImage.addEventListener('click',function() {goBackToSmall();});
imageChild.addEventListener('click',function() {doNothing(event);});

function displayLargeImage(event){
    displayImage.className = "display_img";
    imageChild.src = event.target.src;
    console.log(event);
    console.log(imageChild);
    console.log(imageChild.src);
}

function goBackToSmall(){
    displayImage.className = "display_none";
}

function doNothing(event){
    event.stopPropagation()
}

changeName();
function changeName(){   // if the will support it continue
    var str = document.getElementsByClassName("tagline");   //Making a var for the string on the HTML
    var name = sessionStorage.getItem('name');  //Getting the item from sessionStorage
    console.log(name);
    document.body.innerHTML = document.body.innerHTML.replace(/tiffany/g, name);

}





