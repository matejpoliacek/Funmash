var imgs = document.getElementsByTagName('img');

        // Default: Bubbling
        for(var i=0; i<imgs.length; i++) {
          imgs[i].addEventListener("click", doSomething);
        }
		
		function doSomething() {
            alert(this.className);
        }

function getImageName(element) {
	var src = element.src;
	return src;
}


		

function zpopup(img) {
       //var image = getImageName(); //$(this).attr('src');
		var source = getImageName(img);
		var newImg = document.createElement("img")
		newImg.setAttribute('src', source);
		console.log(newImg)
        w2popup.open({
            title: 'Image',
            body: '<div class="w2ui-centered"><img class="popup" src="'+source+'"></img></div>',
			width: getWidth(newImg),
			height: getHeight(newImg)
        });
    }


function getWidth(imgFile) {
	var wdBody =  (window.innerWidth || document.body.clientWidth);
	var wdImg = imgFile.naturalWidth * 1.05;
	
	if (wdBody > wdImg) {
		return wdImg;
	} else {
		return wdBody;
	}
}

function getHeight(imgFile) {
	var hgBody = (window.innerHeight || document.body.clientHeight);
	var hgImg = imgFile.naturalHeight * 1.1;
	if (hgBody > hgImg) {
		return hgImg;
	} else {
		return hgBody;
	}
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