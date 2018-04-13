$(function () {
    $("input:checkbox").change(function() {
        if($("input:checkbox:checked").length) {
            $("#delete-files").prop("disabled", false);
        }
        else {
            $("#delete-files").prop("disabled", true);
        }
    });
    $("#delete-files").on('click', function () {
        var ids = [];
        if($("input:checkbox:checked").length) {
            $("input:checkbox:checked").each(function () {
                ids.push($(this).val());
            })
        }
        if(ids.length){
            ids = ids.join(",");
            var file_ids = {'ids': ids};
            $.post('/delete/', file_ids, function (data, status) {
                console.log(status);
            })
        }
    })
});
