/**
* Created by Chelsea on 9/1/15.
*/

///--------------------------------------------------------------------------------------------
var $position=("#gallery");
var $displayImage=("#image_show");
var $imageChild=("div img:first-child");
var $images = [];

//$("li").each(function() {
( function () {
    for (var i=1; i<=60; i ++) {
        if (i<=9){
            $images.push("images/pdxcg_0" + i + ".jpg");

        } else {
            $images.push("images/pdxcg_" + i + ".jpg");
        }
    }
}());

var items = [];
jQuery.each($images, function(i, item) {
  items.push('<li><img src=' + item + '></li>')
});
$("#gallery").append(items);

changeName();
//HAVE NOT CHANGED////////////////
function changeName() {   // if the will support it continue
    //var str = document.getElementsByClassName("tagline");   //Making a var for the string on the HTML
    var name = sessionStorage.getItem('name');  //Getting the item from sessionStorage
    console.log(name);
    document.body.innerHTML = document.body.innerHTML.replace(/tiffany/g, name);
}
/////////////////////

$($position).on( "click", function(event) {
    $("li").addClass('display_none');
    $($displayImage).attr('class', 'display_img');
    $($imageChild).attr('src', event.target.src);
    console.log(event.target.src);
  console.log("We are here!");
});

$($imageChild).on( "click", function(event) {
    event.stopPropagation()
});

$($displayImage).on("click", function(event){
        $($displayImage).attr('class', 'display_none');
        console.log("Crosses fingers")
    }
);
///--------------------------------------------------------------------------------------------