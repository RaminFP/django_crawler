$(document).ready(function(){

        $("#go").click(function(){
        $("#imgsearch").hide();
        $("#textform").css({"margin-top":"-300px"});
        var text = $("#textbox").val().length;
        if(text > 0)
            return true;
        else
            return false;

    });
});