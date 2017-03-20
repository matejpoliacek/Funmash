var imgs = document.getElementsByTagName('img');

        // Default: Bubbling
        for(var i=0; i<imgs.length; i++) {
          imgs[i].addEventListener("click", doSomething);
        }
		
		function doSomething() {
            alert(this.className);
        }

var getImageName = function() {
	document.onclick = function(e) {
		if (e.target.tagName == 'IMG') {
			var image = e.target.getAttribute("src");
		}
	}
}

function zpopup() {
       //var image = getImageName(); //$(this).attr('src');
        w2popup.open({
            title: 'Image',
            body: '<div class="w2ui-centered"><img src="'+getImageName()+'"></img></div>'
        });
    }


	/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
    document.getElementById("mySideBar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNav() {
    document.getElementById("mySideBar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "#ffe29b";
}


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