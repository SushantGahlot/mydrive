$(function () {
    var category = $(".old-category").html();

    $("input:radio").change(function () {
        if ($("input:radio:checked").val() !== category) {
            $(".save-category").prop('disabled', false);
        }
        else {
            $(".save-category").prop('disabled', true);
        }
    });
    $(".save-category").on('click', function () {
        var new_category = $("input:radio:checked").val();
        if (new_category !== category) {
            var data = {'category': new_category};
            $.post(window.location.pathname, data, function (data, status) {
                if (status === 'success') {
                    $(".old-category").html(new_category);
                    category = new_category;
                    $("#changeCategory").modal("hide");
                    new Noty({
                        type: 'success',
                        timeout: 2000,
                        text: 'Category successfully changed'
                    }).show();
                }
                else {
                    new Noty({
                        type: 'error',
                        timeout: 5000,
                        text: 'Oops ! There seems to be some problem. Please try again later.'
                    }).show();
                }
            })
        }
    });
    $(".delete-file").on('click', function () {
        var ids = [];
        ids = window.location.pathname;
        ids = ids.split("/");
        ids = ids[2];
        if (ids.length) {
            var file_ids = {'ids': ids};
            $.post('/delete/', file_ids, function (data, status) {
                if (status === 'success') {
                    if (window.location.pathname === "/home/") {
                        for (var i = 0; i < ids.length; i++) {
                            var row = $(".row-" + ids[i]);
                            row.remove();
                            $("#delete-files").prop("disabled", true);
                        }
                    }
                    else {
                        window.location.pathname = '/home/';
                    }
                }
                else {
                    new Noty({
                        type: 'error',
                        timeout: 5000,
                        text: 'Oops ! There seems to be some problem with deleting files. Please try again later.'
                    }).show();
                }
            })
        }
    })
});
