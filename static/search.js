$(document).ready(function (event) {

    $("#search-form").submit(function (event) {

        event.preventDefault();
        alert("submit click");
        $.ajax({
            url: $(this).attr("js-search-url"),
            type: $(this).attr("method"),
            data: $(this).serialize(),
            dataType: 'json',
            success: function (data) {
                
                if (data.isSuccess)
                    alert("data saved successfully");
            },

            error: function (request, status, error) {
                alert("error");
                
            }
        });


    });
});
