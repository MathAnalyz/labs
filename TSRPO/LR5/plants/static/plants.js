$(function () {

  /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-plant").modal("show");
            },
            success: function (data) {
                $("#modal-plant .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-plant").modal("hide");
                    $("#plants-blog").html(data.html_plants_blog);
                }
                else {
                    $("#modal-plant .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };

  /* Binding */

  // Delete plant
    $(".blog-main").on("click", ".js-delete-plant", loadForm);
    $("#modal-plant").on("submit", ".js-plant-delete-form", saveForm);

    var num = 2; //чтобы знать с какой записи вытаскивать данные
    var loading = function() {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: "get",
            data: {"num": num},
            dataType: 'json',
            cache: false,
            success: function(data){
                if(data.none){  // смотрим ответ от сервера и выполняем соответствующее действие
                    alert("Больше нет записей");
                }else{
                    $("#plants-blog").html(data.html_plants_blog);
                    num = num + 2;
                }
            }
        });
    };

    $("#load").on("click", loading);
});
