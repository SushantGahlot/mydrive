$(function () {

    $(document).on("change", "input:checkbox", function () {
        if ($("input:checkbox:checked").length) {
            $("#delete-files").prop("disabled", false);
        }
        else {
            $("#delete-files").prop("disabled", true);
        }
    });
    $("#delete-files").on('click', function () {
        var ids = [];
        if ($("input:checkbox:checked").length) {
            $("input:checkbox:checked").each(function () {
                ids.push($(this).val());
            })
        }
        if (ids.length) {
            var id_string = ids.join(",");
            var file_ids = {'ids': id_string};
            $.post('/delete/', file_ids, function (data, status) {
                if (status === 'success') {
                    for (var i = 0; i < ids.length; i++) {
                        var row = $(".row-"+ids[i]);
                        row.remove();
                        $("#delete-files").prop("disabled", true);
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
