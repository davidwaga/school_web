$('input[name="checkbox"]').click(function() {
    data['checked'] = $(this).value()
    $.ajax({
        url: 'save_state/',
        type: 'POST',
        data: data
    });
});