var searchvisible = 0;

$("#search-menu").click(function(e){ 
    //This stops the page scrolling to the top on a # link.
    e.preventDefault();

    var val = $('#search-icon');
    if(val.hasClass('ion-ios-search-strong')){
        val.addClass('ion-ios-close-empty');
        val.removeClass('ion-ios-search-strong');
    }
    else{
         val.removeClass('ion-ios-close-empty');
        val.addClass('ion-ios-search-strong');
    }
    
    
    if (searchvisible ===0) {
        //Search is currently hidden. Slide down and show it.
        $("#search-form").slideDown(200);
        $("#s").focus(); //Set focus on the search input field.
        searchvisible = 1; //Set search visible flag to visible.
    } 

    else {
        //Search is currently showing. Slide it back up and hide it.
        $("#search-form").slideUp(200);
        searchvisible = 0;
    }
});

/*!
 * classie - class helper functions
 * from bonzo https://github.com/ded/bonzo
 * 
 * classie.has( elem, 'my-class' ) -> true/false
 * classie.add( elem, 'my-new-class' )
 * classie.remove( elem, 'my-unwanted-class' )
 * classie.toggle( elem, 'my-class' )
 */

/*jshint browser: true, strict: true, undef: true */
/*global define: false */

( function( window ) {

'use strict';

// class helper functions from bonzo https://github.com/ded/bonzo

function classReg( className ) {
  return new RegExp("(^|\\s+)" + className + "(\\s+|$)");
}

// classList support for class management
// altho to be fair, the api sucks because it won't accept multiple classes at once
var hasClass, addClass, removeClass;

if ( 'classList' in document.documentElement ) {
  hasClass = function( elem, c ) {
    return elem.classList.contains( c );
  };
  addClass = function( elem, c ) {
    elem.classList.add( c );
  };
  removeClass = function( elem, c ) {
    elem.classList.remove( c );
  };
}
else {
  hasClass = function( elem, c ) {
    return classReg( c ).test( elem.className );
  };
  addClass = function( elem, c ) {
    if ( !hasClass( elem, c ) ) {
      elem.className = elem.className + ' ' + c;
    }
  };
  removeClass = function( elem, c ) {
    elem.className = elem.className.replace( classReg( c ), ' ' );
  };
}

function toggleClass( elem, c ) {
  var fn = hasClass( elem, c ) ? removeClass : addClass;
  fn( elem, c );
}

var classie = {
  // full names
  hasClass: hasClass,
  addClass: addClass,
  removeClass: removeClass,
  toggleClass: toggleClass,
  // short names
  has: hasClass,
  add: addClass,
  remove: removeClass,
  toggle: toggleClass
};

// transport
if ( typeof define === 'function' && define.amd ) {
  // AMD
  define( classie );
} else {
  // browser global
  window.classie = classie;
}

})( window );

// (function() {
//     var triggerBttn = document.getElementById( 'trigger-overlay' ),
//         overlay = document.querySelector( 'div.overlay' ),
//         closeBttn = overlay.querySelector( 'button.overlay-close' );
//         transEndEventNames = {
//             'WebkitTransition': 'webkitTransitionEnd',
//             'MozTransition': 'transitionend',
//             'OTransition': 'oTransitionEnd',
//             'msTransition': 'MSTransitionEnd',
//             'transition': 'transitionend'
//         },
//         transEndEventName = transEndEventNames[ Modernizr.prefixed( 'transition' ) ],
//         support = { transitions : Modernizr.csstransitions };

//     function toggleOverlay() {
//         if( classie.has( overlay, 'open' ) ) {
//             classie.remove( overlay, 'open' );
//             classie.add( overlay, 'close' );
//             var onEndTransitionFn = function( ev ) {
//                 if( support.transitions ) {
//                     if( ev.propertyName !== 'visibility' ) return;
//                     this.removeEventListener( transEndEventName, onEndTransitionFn );
//                 }
//                 classie.remove( overlay, 'close' );
//             };
//             if( support.transitions ) {
//                 overlay.addEventListener( transEndEventName, onEndTransitionFn );
//             }
//             else {
//                 onEndTransitionFn();
//             }
//         }
//         else if( !classie.has( overlay, 'close' ) ) {
//             classie.add( overlay, 'open' );
//         }
//     }

//     triggerBttn.addEventListener( 'click', toggleOverlay );
//     closeBttn.addEventListener( 'click', toggleOverlay );
// })();


// comment-quote
function commentQuote(id,name){
  var eleSelector = '#comment-quote-' + id 
  var quoteValue = $(eleSelector).children().clone().children('blockquote').remove().end().html()
  var textAreaValue = '<blockquote>\n' + '<pre>引用<a href="#comment-' + id +'">'+ name +  '的发言</a>:</pre>\n' + $.trim(quoteValue) + '\n</blockquote>\n'
  var textAreaNode = $('#id_text')
  textAreaNode.val(textAreaValue)
  setTimeout(function(){textAreaNode.focus()},500) 
  
 
}

function validateCommentForm() {
  var form = document.forms["commentForm"]
  var text = form["text"];
  var name = form["name"];
  var email = form["email"];
  var url = form["url"];
  var text_error = $('#comment-text-error')
  var name_error = $('#comment-name-error')
  var email_error = $('#comment-email-error')
  var url_error = $('#comment-url-error')
  var validity = true
  var reg_email=/^[a-z0-9](\w|\.|-)*@([a-z0-9]+-?[a-z0-9]+\.){1,3}[a-z]{2,4}$/i;
  var reg_url=/^((https|http|ftp|rtsp|mms){0,1}(:\/\/){0,1})www\.(([A-Za-z0-9-~]+)\.)+([A-Za-z0-9-~\/])+$/i;
  // 留言校验
  var text_value = $.trim(filterXSS(text.value));
  
  
  

  if(text.value){
    text_error.html("")
    if(text.value.match(/<blockquote>/g)){
      const parser = new DOMParser()
      const doc = parser.parseFromString(text.value,'text/html')
      doc.querySelector('blockquote').remove()
      const value = doc.querySelector('body').innerHTML.replace(/[\r\n]/g,'')
      
      if(!value){
        text_error.html("留言内容不能为空")
        validity = false
      }
      if(value.length > 1000){ 
        text_error.html("留言长度过长，支持1000字符以内")
        validity = false;
      }
    }else if(text.value.length > 1000){ 
      text_error.html("留言长度过长，支持1000字符以内")
      validity = false;
    }
  }else{
    text_error.html("留言内容不能为空")
    validity = false;
  };
 
  // 名字校验
  if(name.value){
    name_error.html("")
    if(name.value.length > 50){ 
      name_error.html("名字长度过长,支持50字符以内")
      validity = false;
    };
  }else{ 
    name_error.html("名字不能为空")
    validity = false;
  };
  // 邮箱校验
  if(email.value){
    email_error.html("")
    if(email.value.length > 100){ 
      email_error.html("邮箱长度过长,支持100字符以内")
      validity =false;
    }else if(!email.value.match(reg_email)){
      email_error.html("邮箱格式不正确")
      validity = false;
    }
  }else{
    email_error.html("邮箱不能为空")
    validity = false;
  };
  // 网址校验
  if(url.value){
    url_error.html("")
    if(url.value.length > 200){ 
      url_error.html("网址长度过长,支持200字符以内")
      validity = false;
    }else if(!url.value.match(reg_url)){
      url_error.html("网址格式不正确")
      validity = false;
    }
  }
  if(validity){
    text.value =text_value
    // form.submit()
  }else{
    return false
  }
  
}