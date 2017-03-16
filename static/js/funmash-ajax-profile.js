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
				$.get('/funmash_app/uploaded/', {}, function(data) {
					$('#uploaded').html(data);
					document.getElementById("ifsuccess").innerHTML = "succesfuly uploaded!";
					
				
			});
				
            },
            error: function(data){
                console.log("error");
                console.log(data);
				
            },
			
        });
			
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
});