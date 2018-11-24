CKEDITOR.instances.text.on('change', function() { 
     var areaText = CKEDITOR.instances['text'].getData();
    console.log(areaText)
    $('#texto').val(areaText); 
});