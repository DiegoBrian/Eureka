$(document).ready( function () {
	$("#tabela_conteudos").hide();
	$("#tabela_outras_turmas").hide();
	$("#btn_turmas").trigger('click');
	$("#btn_minhas_turmas").trigger('click');
});

$('#btn_turmas').click(function() {
	$("#tabela_conteudos").hide();	
	$("#tabela_turmas").show();	
});

$('#btn_conteudos').click(function() {
	$("#tabela_turmas").hide();	
	$("#tabela_conteudos").show();	
});

$('#btn_outras_turmas').click(function() {
	$("#tabela_minhas_turmas").hide();	
	$("#tabela_outras_turmas").show();	
});

$('#btn_minhas_turmas').click(function() {
	$("#tabela_outras_turmas").hide();	
	$("#tabela_minhas_turmas").show();	
});