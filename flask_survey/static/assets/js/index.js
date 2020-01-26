Survey.StylesManager.applyTheme("bootstrap");

var uid = $("#uid").html();
var postid = $("#postid").html();


var surveyJSON = { surveyId: uid};

function sendDataToServer(survey) {
    survey.sendResult(postid);
}

var survey = new Survey.Model(surveyJSON);
$("#surveyContainer").Survey({
    model: survey,
    onComplete: sendDataToServer
});


$("#question_type").change(function() {
    if ($("#question_type").val() == "radiogroup") {
        console.log("asdas");
        $("#radio_choices").attr("style", "display: block")
    }
        else {
        $("#radio_choices").attr("style", "display: none")
    }
});
