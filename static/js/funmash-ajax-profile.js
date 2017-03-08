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
			});
				
            },
            error: function(data){
                console.log("error");
                console.log(data);
            },
			
        });
		document.getElementById("ifsuccess").innerHTML = "succesfuly uploaded!";		
    }));

    $("#ImageBrowse").on("change", function() {
        $("#imageUploadForm").submit();
    });
	
	$('#input_pic').on('change', function(e) {
		document.getElementById("ifsuccess").innerHTML = "";
	});
	
	$('#next').click(function() {
		
	});
});