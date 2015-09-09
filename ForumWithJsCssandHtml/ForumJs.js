/**
 * Created by Chelsea on 9/8/15.
 */


//function postThePost(){
//console.log();
    //console.log('test');


//}

$.ajax({
url: 'https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script',
type: "GET",
dataType: "jsonp",
complete: function(data) {

    //console.log("Bruh");
    console.log(data.responseJSON.feed.entry);
    var object = data.responseJSON.feed.entry;
    //var id = data.feed.entry[i].id.$t;
    //var title = object.title.$t;
    var string = "<ul>";
    //var content = data.feed.entry[i].content.$t;
    //console.log(object.gsx$posttitle);
    for (var i=0; i < object.length; i++) {
        //console.log(title);
        var itemtitle = data.responseJSON.feed.entry[i].gsx$posttitle.$t;
        var itembody = data.responseJSON.feed.entry[i].gsx$postbody.$t;

        string += '<li>'+itemtitle+'<br>'+itembody+'</li>';

        $( 'body' ).append(string);
        //var id = data.feed.entry[i].id.$t;
        //console.log(object.gsx$posttitle.$t);
        //console.log(object['gsx$posttitle']);
        //var fucku = ['<li><p>' + i + 'object.gsx$posttitle.$t' + '</p></li>'];
        //console.log('object.gsx$posttitle.$t.posttitle');
        //$( 'main' ).append(fucku);
        //$( 'main' ).append('<li><p>' + i  + '</p></li>');
        //$( 'main').append('<li>'+ i + object.gsx$posttitle.$t +'</li>');

        //$(' main ').append(['object']['gsx$posttitle']['$t']);
    //    $(object).push('test');
    //var inputtitle=$('input[name=posttitle]').val();
    //console.log(inputtitle);
    }
}
});
