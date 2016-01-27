//this code needed for identification for vk 
// vk init
VK.init({
	apiId: 5238735, 
	onlyWidgets: true
});

// vk auth login
VK.Auth.getLoginStatus(function(response) {
	if (response.session) {
		if (window.location.pathname == "/") {
			window.location.href = '/blogs/';
		} 
	} 
});


// $(document).ready(function(){
//     $("#comments").on("click", ".reply", function(event){
//         event.preventDefault();
//         var form = $("#comment_post").clone(true);
//         form.find('.parent').val($(this).parent().parent().attr('id'));
//         $(this).parent().append(form);
//     });
// });