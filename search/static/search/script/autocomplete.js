
(function (jq) {
    jq("#action1").click(function () {
    var value = $(this).val();
    $.ajax({
        type: "GET",
        url: "search",
        async: true,
        data: {
            word : value // as you are getting in php $_POST['action1']
        },
        success: function (msg) {
            alert('Success');
            if (msg != 'success') {
                alert('Fail');
            }
        }
    });
});

})(django.jQuery);