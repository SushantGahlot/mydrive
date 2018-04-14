$(function () {
    $('#autocomplete').autocomplete({
        serviceUrl: '/search-files/',

        onSelect: function (suggestion) {
            window.location.pathname = '/file/' + suggestion.data+'/';
        }
    })
});