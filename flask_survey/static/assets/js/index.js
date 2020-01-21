Survey.StylesManager.applyTheme("darkblue");

var surveyJSON = { surveyId: 'ee67b846-7a75-44af-9ea4-ab88714fde70'};

function sendDataToServer(survey) {
    survey.sendResult('001e5548-22c9-48e2-a577-e081733bb173');
}

var survey = new Survey.Model(surveyJSON);
$("#surveyContainer").Survey({
    model: survey,
    onComplete: sendDataToServer
});

// Survey.StylesManager.applyTheme("bootstrap");
//
// var surveyJSON = {locale:"de",pages:[{name:"page1",elements:[{type:"rating",name:"question1",title:{de:"Wie hat Ihnen die heutige Veranstaltung gefallen?"},minRateDescription:{de:"Überhaupt nicht"},maxRateDescription:{de:"Sehr gut"}}]},{name:"page2",elements:[{type:"panel",name:"panel2",elements:[{type:"boolean",name:"question2pie",title:{de:"... ausreichend repräsentiert"},labelTrue:{default:"Yes",de:"Ja"},labelFalse:{default:"No",de:"Nein"}},{type:"boolean",name:"question3pie",title:{de:"... ausreichend informiert?"},labelTrue:{default:"Yes",de:"Ja"},labelFalse:{default:"No",de:"Nein"}}],title:{de:"Fühlen Sie sich innerhalb des Entscheidungsprozesses...."}}]},{name:"page3",elements:[{type:"comment",name:"question4input",title:{de:"Welchem Thema wurde ihrer Meinung nach noch nicht genug Beachtung geschenkt?"},placeHolder:{de:"Bitte tragen Sie hier ihr Anlegen ein."}}]},{name:"page4",elements:[{type:"panel",name:"panel1",elements:[{type:"boolean",name:"email_boolean",title:{de:"Wünschen Sie über das Ergebnis der Umfrage informiert zu werden?"},defaultValue:"false",labelTrue:"Yes",labelFalse:"No"},{type:"text",name:"email_input",visibleIf:"{email_boolean} = true",indent:4,title:{de:"email_input"},titleLocation:"hidden",inputType:"email",placeHolder:{de:"Geben Sie hier ihre Email-Adresse ein."}},{type:"boolean",name:"mail_further_info",title:{de:"Möchten Sie gerne weiteres Infomaterial zum Thema der heutigen Veranstaltung erhalten?"},defaultValue:"false",labelTrue:"Yes",labelFalse:"No"}]}]}],showProgressBar:"both",goNextPageAutomatic:true}
//
// function sendDataToServer(survey) {
//     survey.sendResult('001e5548-22c9-48e2-a577-e081733bb173');
// }
//
// var survey = new Survey.Model(surveyJSON);
// $("#surveyContainer").Survey({
//     model: survey,
//     onComplete: sendDataToServer
// });