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
