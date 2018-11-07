$( '#id_quesion_type' ).click(function() {
	if ($('#id_quesion_type').val() == 'ABERTA'){
		$("#id_answer_a").hide();
		$('label[for="id_answer_a"]').hide()
        $("#id_answer_b").hide();
        $('label[for="id_answer_b"]').hide()
        $("#id_answer_c").hide();
        $('label[for="id_answer_c"]').hide()
        $("#id_answer_d").hide();
        $('label[for="id_answer_d"]').hide()
        $("#id_correct_answer").hide();
        $('label[for="id_correct_answer"]').hide()
	}
	else{
		$("#id_answer_a").show();
		$('label[for="id_answer_a"]').show()
        $("#id_answer_b").show();
        $('label[for="id_answer_b"]').show()
        $("#id_answer_c").show();
        $('label[for="id_answer_c"]').show()
        $("#id_answer_d").show();
        $('label[for="id_answer_d"]').show()
        $("#id_correct_answer").show();
        $('label[for="id_correct_answer"]').show()
	}
})