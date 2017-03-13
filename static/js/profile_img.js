var getImageName = function() {
	document.onclick = function(e) {
		if (e.target.tagName == 'IMG') {
			var image = e.target.getAttribute("src");
		}
	}
}

getImageName();