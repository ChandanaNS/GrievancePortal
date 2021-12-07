$(document).ready(function () {
	/* load json file form Database */

	var dataVar;
	var adminUser = 'false';
	if (typeof data != "undefined" && data != null) {

	    if(data['superAdmin'] && data['superAdmin'] == 'true'){
	        adminUser = 'true';
	    }
		userData = data.userList;
		dataVar= data.adminGrievanceList ?  data.adminGrievanceList : data.grievanceList;
	}
	jQuery(function ($) {
      $('form').bind('submit', function () {
        $(this).find(':input').prop('disabled', false);
      });
    });

	//  update function
	if (typeof update != "undefined" && update != null) {
        console.log("update", update);
		const grievanceToUpdate = update['GrievanceList'][0];
		$('#grievanceId').val(grievanceToUpdate["id"]);
		$('#category').val(grievanceToUpdate["category"]);
		$('#status').val(grievanceToUpdate["status"]);
		$('#description').val(grievanceToUpdate["description"]);
		$('#raisedUser').val(grievanceToUpdate["raisedUser"]);
		$('#reply').val(grievanceToUpdate["reply"]);
		if(update['AdminUser'] != 'True'){
            $('#raisedUser').prop( "disabled", true );
            $('#reply').prop( "disabled", true );
		}else{
		    $('#description').prop( "disabled", true );
		}
	}
	//navigation css
	$("body").on("click", ".nav-link", function () {
		$(this).toggleClass('text-danger');
	});
//
    //flash message for 4s
	setTimeout(function () {
		$('.alert-warning').remove();
	}, 4000);

//
//	//category filter
//	var filterCategory = dataVar.reduce(
//		(obj, item) => Object.assign(obj, {
//			[item.category]: item.status
//		}), {}
//	);
//
//
//	//Category filter option
//	$("body").on("click", ".filter-pills", function () {
//		$(this).toggleClass('active');
//		var selectedItems = [];
//		$(".filter-pills").each(function () {
//			if ($(this).hasClass("active")) {
//				selectedItems.push($(this).attr("category"));
//			}
//		});
//		var filteredItems;
//		if (selectedItems.length != 0) {
//			filteredItems = dataVar.filter(function (item) {
//				return selectedItems.indexOf(item.category) > -1;
//			});
//		} else {
//			filteredItems = dataVar;
//		}
//		viewProducts(filteredItems);
//	});
//
//	//filter nav pills
//	$.each(Object.keys(filterCategory), function (index, item) {
//		var categoryString =
//			' <a class="filter-pills" href="#" category="' +
//			item +
//			'">' +
//			item +
//			"</a>";
//		$(".category-listing-navigation-pills").append(categoryString);
//	});

	//render template for grievances
	function viewGrievances(dataVar) {
	console.log("datavar", dataVar.length)
		var templateString = '';
		if(dataVar.length == 0){
		 templateString += '<div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 m-auto">No records Found</div>'
		} else{$.each(dataVar, function (index, value) {
		    console.log(index, value, data)
			if (data['superAdmin'] && data['superAdmin'] == 'true') {
			    templateString +=
					'<tr><td scope="row">'+(index+1)+'</td><td>'+value['description']+'</td><td>'+value['category']+
					'</td><td>'+value['status']+'</td><td>'+value['raisedUser']+'</td>'+
					'<td> <a href="/update?id=' + value['id'] + '" class="updateButton">Reply</a></td>'
			} else {
			    console.log(value);
				templateString +=
					'<tr><td scope="row">'+(index+1)+'</td><td>'+value['description']+'</td><td>'+value['category']+
					'</td><td>'+value['status']+'</td><td>'+value['reply']+'</td>'+
					'<td> <a href="/update?id=' + value['id'] + '" class="updateButton">EDIT</a></td>'

			}
		});

		}
		$("#grievances").html(templateString);
	}

	viewGrievances(dataVar);


	//render template for users
	function viewUsers(userData) {
		var templateString = '';
		$.each(userData, function (i) {
			if (data['superAdmin'] == 'true') {
				templateString += '<tr><th scope="row">' +
					userData[i].loginId + '</th><td >' + userData[i].userName + '</td><td >' + userData[i].dateOfBirth +
					'</td><td >' + userData[i].email + '</td><td >' + userData[i].gender + '</td><td >' +
					userData[i].name + '</td><td >' + userData[i].phoneNumber + '</td></tr>';
			}
		});
		var tableString = '<div class="tableClass"><div class="table-responsive"><table class="table "><thead class="thead-dark"><tr><th scope="col">UserId</th>' +
			'<th scope="col">User Name</th><th scope="col">Date of Birth</th><th scope="col">Email</th>' +
			'<th scope="col">Gender</th><th scope="col">Name</th><th scope="col">Phone Number</th>' +
			'</tr></thead><tbody>' +
			templateString +
			'</tbody></table></div></div>';
		$("#grievances").html(tableString);
	}


    //fetch user details
	$("body").on("click", ".user-statistic", function (event) {
		event.preventDefault();
		$('nav').find('.text-danger').removeClass('text-danger');
		$(this).addClass('text-danger');
		$('body').find('.thead-dark').addClass('d-none');
		viewUsers(userData);
	});


});