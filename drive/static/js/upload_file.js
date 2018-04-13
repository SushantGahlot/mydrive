$(function () {
    $(".js-upload-photos").click(function () {
        $("#exampleModal").modal('show');
        // $("#id_file").click();
    });

    $("#fileupload").fileupload({
        dataType: 'json',
        sequentialUploads: true,
        change: function (e, data) {
            $(".filename").html("File chosen: "+data.files[0].name);
        },
        add: function (e, data) {
            $("#save").off('click').on('click', function () {
                e.preventDefault();
                var category = "";
                if ($('.form-check-input').is(':checked')) {
                    category = $('.form-check-input:checked').val();
                    data.formData = {
                        'category': category,
                        'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
                    };
                    data.submit();
                    $("#exampleModal").modal('hide');
                }
                else {
                    new Noty({
                        type: 'error',
                        timeout: 3000,
                        text: 'Please select category'
                    }).show();
                }
            })
        },
        start: function (e) {
            $("#modal-progress").modal("show");
        },

        stop: function (e) {
            $("#modal-progress").modal("hide");
        },

        progressall: function (e, data) {
            var progress = parseInt(data.loaded / data.total * 100, 10);
            var strProgress = progress + "%";
            $(".progress-bar").css({"width": strProgress});
            $(".progress-bar").text(strProgress);
        },

        done: function (e, data) {
            if (data.result.is_valid) {
                $('.form-check-input').prop('checked', false);
                $("#gallery tbody").prepend(
                    "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
                )
            }
        }

    });

});
