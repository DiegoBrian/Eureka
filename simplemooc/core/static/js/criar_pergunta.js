$( '#id_quesion_type' ).click(function() {
	console.log($('#id_quesion_type').val())
	if ($('#id_quesion_type').val() == 'ABERTA'){
		$("#answer_a-div").hide();
		$("#answer_b-div").hide();
		$("#answer_c-div").hide();
		$("#answer_d-div").hide();
		$("#answer_e-div").hide();
		$("#correct_answer-div").hide();
	}
	else{
		$("#answer_a-div").show();
		$("#answer_b-div").show();
		$("#answer_c-div").show();
		$("#answer_d-div").show();
		$("#answer_e-div").show();
		$("#correct_answer-div").show();
	}
})