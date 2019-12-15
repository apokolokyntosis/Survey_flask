Survey.StylesManager.applyTheme("bootstrap");

var surveyJSON = {
    pages: [{
        name: "page1",
        elements: [{type: "checkbox", name: "question1", choices: ["item1", "item2", "item3"]}]
    }, {name: "page2", elements: [{type: "text", name: "question2"}]}, {
        name: "page3",
        elements: [{type: "boolean", name: "question3", labelTrue: "Yes", labelFalse: "No"}]
    }]
}

function sendDataToServer(survey) {
    survey.sendResult('b3d53e73-709a-40eb-b8c6-8a7ec38d050c');
}

var survey = new Survey.Model(surveyJSON);
$("#surveyContainer").Survey({
    model: survey,
    onComplete: sendDataToServer
});