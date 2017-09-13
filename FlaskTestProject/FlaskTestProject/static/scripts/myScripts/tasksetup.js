$(document).ready(function () {
    //$('.fileUploaderForm').submit(function (e) {
    //    e.preventDefault();
    //    var formdata = new FormData(this);
    //    $.post($(this).attr('action'), formdata, function (data) {
    //        alert(data);
    //    });
    //    return false;
    //})

    $('.fileUploaderForm').on('submit', function (e) {
        e.preventDefault();

        var formdata = new FormData(this);
        $.ajax({
            url: $(this).attr('action'),
            type: "POST",
            data: formdata,
            contentType: false,
            processData: false,
            success: function (data) {
                alert('Upload File Successed');
            },
            error: function (jXHR, textStatus, errorThrown) {
                alert(errorThrown);
            }
        })
    })
});
