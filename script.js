// function for learning suggestion
// I learned this from sololearn
$(function() {
    $("#add").on("click", function() {
        var val = $("input").val();
        if(val !== '') {
            var elem = $("<li></li>").text(val);
            $(elem).prepend("<button class='rem'>X</button>");
            $("#mylist").prepend(elem);
            $("input").val("");
            $(".rem").on("click", function() {
                $(this).parent().remove();
            });
        }
    });
});

