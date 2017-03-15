var getImageName = function() {
	document.onclick = function(e) {
		if (e.target.tagName == 'IMG') {
			var image = e.target.getAttribute("src");
		}
	}
}

function popup() {
       //var image = getImageName(); //$(this).attr('src');
        w2popup.open({
            title: 'Image',
            body: '<div class="w2ui-centered"><img src="'+getImageName()+'"></img></div>'
        });
    }
	
	
//fadeout
setTimeout(function() { // start a delay
  var fade = document.getElementById("fade"); // get required element
  fade.style.opacity = 1; // set opacity for the element to 1
  var timerId = setInterval(function() { // start interval loop
    var opacity = fade.style.opacity; // get current opacity
    if (opacity == 0) { // check if its 0 yet
      clearInterval(timerId); // if so, exit from interval loop
    } else {
      fade.style.opacity = opacity - 0.05; // else remove 0.05 from opacity
    }
  }, 100); // run every 0.1 second
}, 3000)