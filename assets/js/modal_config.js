$(function() {
    $(".modal").easyModal();

    $(".add_topic").click(function() {
        $(".modal").trigger("openModal");
    });
});




