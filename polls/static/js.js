var feedback = 0;

function showAccount() {

    //alert("clicked");
    if (feedback == 0) {
        document.getElementById("js-account").style = "display:block";

        feedback = 1;
    } else {

        document.getElementById("js-account").style = "display:none";

        feedback = 0;
    }


}



////////////////////


// using jQuery
function getCookie(name) {

    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);

            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {

                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
var csrftoken = getCookie('csrftoken');



function addToBasket(){

   
    var url = $("#url-details").attr("data-url");
    
    quan=$("#js-quantity").val()
      var data1 = {
        "quantity": quan,

    };



    $.ajax({
        url: url,
        type: "post",
        data: data1,
        crossDomain: false,
        dataType: "json",
        beforeSend: function (xhr, settings) {

            //alert("before send"+csrfSafeMethod(settings.type));
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {

                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function (data) {

            alert('success');

           
        },

    });

}
