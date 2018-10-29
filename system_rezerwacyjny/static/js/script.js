function overlay() {
    el = document.getElementById("overlay");
    el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}

$(function () {
    $('tr > td a').on('click', function (e) {
        alert($(this).parent().find('span').html());
    });
});