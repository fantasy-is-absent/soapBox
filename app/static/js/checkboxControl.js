$cbx_group = $(":checkbox");

$('button[type="submit"]').on('click', function() {
	$cbx_group.attr('required', true);
	
	$cbx_group.each(function(){
		if ($(this).is(":checked")){ 
			$cbx_group.removeAttr('required');
		}
	});
});
