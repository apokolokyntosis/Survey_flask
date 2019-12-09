Survey
    .StylesManager
    .applyTheme("modern");

var json = {
    title: "Bürgerumfrage",
    goNextPageAutomatic: true,
    showNavigationButtons: true,
    showProgressBar: "bottom",
    surveyPostId : "3c0aafa2-4f26-4aba-b8bd-31e9a9762690",
    pages: [
        {
            name: "page0",
            elements: [
                {
                    "type": "emotionsratings",
                    "name": "emotionsratings-widget",
                    "title": "Wie zufrieden sind Sie mit der Veranstaltung heute?",
                    "choices": ["1", "2", "3", "4", "5"]
                }
            ]
        },
        {
            name: "page1",
            elements: [
                {
                    type: "imagepicker",
                    name: "question1",
                    title: "Wie zufrieden sind sie mit dem heutigen Event?",
                    isRequired: true,
                    choices: [
                        {
                            value: "Positiv",
                            imageLink: "https://www.schilder-klar.de/media/image/e9/45/38/66506001_ef.png"
                        },
                        {
                            value: "Negativ",
                            imageLink: "https://www.clipartwiki.com/clipimg/detail/30-302062_red-sad-face-clip-art-red-sad-smiley.png"
                        }
                    ]
                }
            ]
        },
        {
            name: "page2",
            elements: [
                {
                    type: "radiogroup",
                    name: "question2",
                    title: "Fühlen Sie sich während des Beteiligungsprozesses angemessen repräsentiert?",
                    isRequired: true,
                    colCount: 4,
                    choices: [
                        "-",
                        "o",
                        "+"
                    ],
                    rateMax: 3
                }
            ]
        },
        {
            name: "Email",
            elements: [
                {
                    type: "panel",
                    name: "panel1",
                    elements: [
                        {
                            type: "boolean",
                            name: "mail_boolean",
                            title: "Wünschen Sie, über den Verlauf der Umfrage informiert zu werden?",
                            defaultValue: "false",
                            labelTrue: "Ja",
                            labelFalse: "Nein",
                            showTitle: true
                        },
                        {
                            type: "text",
                            name: "mail_form",
                            visibleIf: "{mail_boolean} = true",
                            title: "Tragen Sie hier ihre Email-Adresse ein, wenn Sie, über die Ergebnisse der Umfrage informiert werden wollen.",
                            inputType: "email",
                            placeHolder: "beispiel@email.com"
                        }
                    ]
                }
            ]
        }
    ],

};

window.survey = new Survey.Model(json);


survey
    .onComplete
    .add(function (result) {
        document
            .querySelector('#surveyResult')
            .textContent = "Result JSON:\n" + JSON.stringify(result.data, null, 3);
    });


$("#surveyElement").Survey({ model: survey });

