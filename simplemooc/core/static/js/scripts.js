$(document).ready( function () {
	$("#div-experimentation_id").hide();
	$("#div-exercise_id").hide();
	$("#div-class_id").hide();
	$('#id_multiple_times').prop('checked', true);
	$("#id_multiple_times").hide();
});

$('#div-exe').click(function() {
	if($("#exe").prop('checked')){
	    $("#div-exercise_id").show();
	}
	else{
	    $("#div-exercise_id").hide();
	    $("#id_exercise_id").val("");
	}

});

$('#div-exp').click(function() {
	if($("#exp").prop('checked')){
	    $("#div-experimentation_id").show();
	}
	else{
	    $("#div-experimentation_id").hide();
	    $("#id_experimentation_id").val("");
	}

});

$('#div-cla').click(function() {
	if($("#cla").prop('checked')){
	    $("#div-class_id").show();
	}
	else{
	    $("#div-class_id").hide();
	    $("#id_class_id").val("");
	}

});

$('#select').click(function() {
	if($("#select").val() == 'sim'){
	    $('#id_multiple_times').prop('checked', true);
	}
	else{
	    $('#id_multiple_times').prop('checked', false);
	}

});