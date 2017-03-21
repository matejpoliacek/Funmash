// $(document).ready(function (e) {

	/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
    document.getElementById("mySideBar").style.width = "450px";
    
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNav() {
    document.getElementById("mySideBar").style.width = "0";
    
}

jQuery(function () {
    var $els = $('p[id^=quote]'),
        i = 0,
        len = $els.length;

    $els.slice(1).hide();
    setInterval(function () {
        $els.eq(i).fadeOut(function () {
            i = (i + 1) % len
            $els.eq(i).fadeIn();
        })
    }, 3500)
})

// Leo text //

// $('#leo').on('click',(function(e) {
// 	var fade = document.getElementById("leotext"); // get required element
//   		fade.style.opacity = 1; // set opacity for the element to 1
// 	document.getElementById("leotext").innerHTML = "Cheers for the feedback!";
// 	var timerId = setInterval(function() { // start interval loop
// 	    var opacity = fade.style.opacity; // get current opacity
// 	    if (opacity == 0) { // check if its 0 yet
// 	      clearInterval(timerId); // if so, exit from interval loop
// 	    } else {
// 	      fade.style.opacity = opacity - 0.05; // else remove 0.04 from opacity
// 	    }
// 	  }, 100); // run every 0.1 second
// 	document.getElementById("leotext").innerHTML = "Tired of scrolling through images? Just click the one you find funnier - and surprise yourself with what comes next. ";
// 	}));

// });

// Matej's original fadeout which Peter modified for success_fadeout in funmash-ajax-profile.js
//fadeout
// setTimeout(function() { // start a delay
//   var fade = document.getElementById("fade"); // get required element
//   fade.style.opacity = 1; // set opacity for the element to 1
//   var timerId = setInterval(function() { // start interval loop
//     var opacity = fade.style.opacity; // get current opacity
//     if (opacity == 0) { // check if its 0 yet
//       clearInterval(timerId); // if so, exit from interval loop
//     } else {
//       fade.style.opacity = opacity - 0.05; // else remove 0.05 from opacity
//     }
//   }, 100); // run every 0.1 second
// }, 3000)