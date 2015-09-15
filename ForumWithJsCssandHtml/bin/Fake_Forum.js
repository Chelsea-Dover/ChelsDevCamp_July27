Fake Forum Code Review
======================

_Review Date: 9/10_

Project Structure
-----------------
- Technically it’s “legal” to have your HTML, CSS, and JS in the same directory no one really does it in practice.
- I’d suggest a structure as follows:
  - I’d advise renaming your only html file `index.html`, if you were to ever wire this in with a webserver, it will make configuration easier.
```
|-ForumWithJsCssandHtml
|- index.html
|- |- css
|--`|- forumcss.css
|- js
|--`|- forumjs.js
```
- currently you’re loading jquery that’s outside of this projects directory, if you don’t want many copies of jquery floating around, you can use the jquery cdn to load it (you’ll need a internet connection) add this to your HTML:
  - `<script src='https://code.jquery.com/jquery-2.1.4.min.js' type="text/javascript"></script>`
  - fwiw your currently solution works, but it doesn’t really work as a “standalone” application.


Overall UI
----------
- Love the handling of the header, the top title disappears, and the form stays.
- not a bad font :-D
- Why is the `post` button so small?
- Kind of wondering why you made the text fields so small?
- think about growing the size of the header and fields when the user clicks in the fields.

HTML
----
- Also you’re using `<input>` on fields `#body`, I’d suggest making that a `<textarea>` it’s better for handling multiline text input
- L13 & L15 label is spelled incorrectly.

JavaScript
----------
- *General Note*:
  - code style try indenting lines inside a function, it will make it easier to tell what’s in a function
- L9 - nice, didn’t know that existed, it’s better than using `success` and `error`, because we have the cross origin error, which causes it to fail
- L10 can be killed.
- L15 - L23 Since you’re only running this once, and doing a hard refresh on the page, it’s best to wrap this as an IFFE. This will free up all the variables, etc because the browser will run it on page load.
```
(function () {
$.ajax({
url: 'https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script',
type: "GET",
dataType: "jsonp",                                                                                                                      }())
complete: function(data) {
    console.log(data.responseJSON);                                                                                                     ```
    var object = data.responseJSON.feed.entry;
    object.reverse();
    for (var i=0; i < object.length; i++) {

        var itemtitle = data.responseJSON.feed.entry[i].gsx$posttitle.$t;
        var itembody = data.responseJSON.feed.entry[i].gsx$postbody.$t;

        var string = '<li>'+itemtitle+'<br>'+itembody+'</li>';

        $( 'body' ).append(string);
    }
}
}()); // make sure you close like this.
```
- L12 kind of dangerous variable name in my opinion. `Object` is a JavaScript thing, and the `var object` could easily confuse you or someone else later.
  - suggest renaming
- L15 and L16 common style of javascript would be `itemBody` but you’re consistent so that’s ok.
- L26 - L34 I’d suggest moving this to the bottom of your script, and keep it will all other event binding
- L36 - I’m not sure you need to worry about the document ready event here. Unlikely that a user will able to scroll until the document is ready.
- L39 - I don’t think you need to set this to be set to a variable. You can make this a named function via `function stickyNav () { // code}`.
- L40 - variable name makes me a bit nervous. The name of the variable is the same as jQuery function, this could easily confuse yourself later.
- L49 - I’m not sure that this is required here. If you load the html page based on the window being at the top of the page, then the correct class should be set. If you call stickNav at that point it won’t do anything. However, I could see there being some possiblilty when a “browser” back button is pressed the browser might load in the middle of the page. So then `stickNav` would need to be called. So maybe it should say.


CSS
---

No real comments here. :)