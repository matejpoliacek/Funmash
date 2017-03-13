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