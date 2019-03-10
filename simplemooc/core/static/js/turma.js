$(document).ready( function () {
	$("#alunos").hide();
	$("#btn_conteudos").trigger('click');
});

$('#btn_alunos').click(function() {
	$("#conteudos").hide();	
	$("#alunos").show();	
});

$('#btn_conteudos').click(function() {
	$("#alunos").hide();	
	$("#conteudos").show();	
});