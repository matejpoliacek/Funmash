$(document).ready(function (e) {
    $('#imageUploadForm').on('submit',(function(e) {
        e.preventDefault();
        var formData = new FormData(this);

        $.ajax({
            type:'POST',
            url: $(this).attr('action'),
            data:formData,
            cache:false,
            contentType: false,
            processData: false,
            success:function(data){
                console.log("success");
                console.log(data);
				document.getElementById("ifsuccess").innerHTML = "succesfuly uploaded!";	
				$.get('/funmash_app/uploaded/', {}, function(data) {
					$('#uploaded').html(data);
					
					
			});
				
            },
            error: function(data){
                document.getElementById("ifsuccess").innerHTML = "not successful! wrong format?";
				console.log("error");
                console.log(data);
				
            },
			
        });
		success_fadeout();
    }));

    $("#ImageBrowse").on("change", function() {
        $("#imageUploadForm").submit();
		
    });
	
	$('#input_pic').on('change', function(e) {
		
	});
	
	$('#next').on('click',function(e) {
		var query;
		
	    query = $('#keepTrack').attr("numOfPicLast");
		
		
		$.get('/funmash_app/next_pic/', {numOfPic : query}, function(data) {
			$('#uploaded').html(data);
	});
	});
	
	$('#previous').on('click',function(e) {		
		var query2;
	    
		query2 = $('#keepTrack').attr("numOfPicFirst");
		
		$.get('/funmash_app/previous_pic/', {numOfFirst : query2}, function(data) {
			$('#uploaded').html(data);
	});
	});

	 function success_fadeout() {
  		var fade = document.getElementById("fade"); // get required element
  		fade.style.opacity = 1; // set opacity for the element to 1
  		var timerId = setInterval(function() { // start interval loop
	    var opacity = fade.style.opacity; // get current opacity
	    if (opacity == 0) { // check if its 0 yet
	      clearInterval(timerId); // if so, exit from interval loop
	    } else {
	      fade.style.opacity = opacity - 0.05; // else remove 0.04 from opacity
	    }
	  }, 100); // run every 0.1 second
	  document.getElementById("ifsuccess").innerHTML = "<br>";
	}
});
