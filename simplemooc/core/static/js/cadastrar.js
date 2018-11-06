$( document ).ready(function() {
    
    if ($('#id_grade').length){
    	$("#id_user_type").val("ALUNO");
        $("#id_grade").attr("min", 6);
    	$("#id_grade").attr("max", 9);
    	$("#id_grade").val(6);
    }
    else{
    	$("#id_user_type").val("PROFESSOR");
    }
});