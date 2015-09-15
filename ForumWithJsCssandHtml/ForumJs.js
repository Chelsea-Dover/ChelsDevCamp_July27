/**
 * Created by Chelsea on 9/8/15.
 */

(function () {
    $.ajax({
        url: 'https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script',
        type: "GET",
        dataType: "jsonp",
        complete: function(data) {

            var foruminfo = data.responseJSON.feed.entry;
            foruminfo.reverse();
            for (var i=0; i < foruminfo.length; i++) {

                var itemTitle = data.responseJSON.feed.entry[i].gsx$posttitle.$t;
                var itemBody = data.responseJSON.feed.entry[i].gsx$postbody.$t;

                var string = '<li>'+itemTitle+'<br>'+itemBody+'</li>';

                $( 'body' ).append(string);
            }
        }
    })
}());

$('#post').on('submit', function (e){
    e.preventDefault();
    var title = $('input[name=posttitle]');
    var body = $('textarea[name=postbody]');
    var post = {'entry_434124687':title.val(), 'entry_1823097801': body.val()};
    $.post(
        'https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse', post);
    location.reload();
});

$(document).ready(function() {
var stickyNavTop = $('.nav').offset().top;

var stickyNav = function(){
var scrollTopPosition = $(window).scrollTop();

    if (scrollTopPosition > stickyNavTop) {
        $('.nav').addClass('sticky');
    } else {
        $('.nav').removeClass('sticky');
    }
};

stickyNav();

$(window).scroll(function() {
    stickyNav();
});
});

$( '#post' ).focusin('click', function(e){
   $( 'form' ).addClass('clicked');
});

$( "#post" ).focusout(function(){
    $( 'form').removeClass('clicked');
});