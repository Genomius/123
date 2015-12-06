$(document).ready(function(){
    $('#id_referrer').after('<a id="parse" href="#">Распарсить</a>');

    $('#parse').click(function(){
        $.ajax({
            url: '/ajax/parse',
            data: {'url' : $('#id_referrer').val()},
            success: function(data){
                $('#id_name').val(data.name);
                $('#id_type').val(data.type);
                $('#id_price').val(data.price);
                $('#id_marking').val(data.marking);
                $('#id_description').val(data.description);

                $('#id_marking').focus();
                $('.default').click();
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});

