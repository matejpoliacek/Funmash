$(document).ready( function(event) {
$('#cimg1').click(function(){		
	    var query;
		
	    query = $('#img1').attr("number");	
	    $.get('/funmash_app/liked_images/', {picture_name: query}, function(data){
	        });
		$.get('/funmash_app/render_pic1/', {}, function(data){
			$('#cimg1').html(data);
			query = $('#img1').attr("number");
			$.get('/funmash_app/render_pic2/', {picture_name: query}, function(data){
				$('#cimg2').html(data);
		});
		});
		
		
		
	});

$('#cimg2').click(function(){		
	    var query;
		
	    query = $('#img2').attr("number");	
	    $.get('/funmash_app/liked_images/', {picture_name: query}, function(data){
	         });
		$.get('/funmash_app/render_pic1/', {}, function(data){
			$('#cimg1').html(data);
			query = $('#img1').attr("number");
			$.get('/funmash_app/render_pic2/', {picture_name: query}, function(data){
				$('#cimg2').html(data);
		});
		});
		
	});	

	

});
