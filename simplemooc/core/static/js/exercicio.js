$(document).ready( function () {
	$("#btn-next").hide();
	$("#btn-finnish").hide();
});

if($("#texto").length > 0 ){
	CKEDITOR.instances.text.on('change', function() { 
	     var areaText = CKEDITOR.instances['text'].getData();
	    $('#texto').val(areaText); 
	    if($('#texto').val().length > 0){
		    $("#btn-next").show();
		    $("#btn-finnish").show();
		}
		else{
		    $("#btn-next").hide();
		    $("#btn-finnish").hide();
		}
	});
}


$("input[name='answer']").change(function(){
	console.log("teste")

	if($('input:radio:checked').length > 0){
		    $("#btn-next").show();
		    $("#btn-finnish").show();
		}
		else{
		    $("#btn-next").hide();
		    $("#btn-finnish").hide();
		}
});

