from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AddQuestionsForm(FlaskForm):
    submit_question = SubmitField("Frage hinzufügen")
    question_title = StringField("Fragentext", validators=[DataRequired()])
    question_type = SelectField("Fragentyp", choices=[("rating", "Numerische Wertung"),
                                                      ("boolean", "Ja/Nein"), ("comment", "Kommentar"),
                                                      ("text", "Text"), ("radiogroup", "Auswahl")],
                                validators=[DataRequired()])
    submit_survey = SubmitField("Umfrage final erstellen")
    radiogroup_choices = StringField("Optionen")


class CreateSurveyForm(FlaskForm):
    create_survey = SubmitField("Umfrage anlegen")
    survey_name = StringField("Name der Umfrage", validators=[DataRequired()])
