from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CreateSurveyForm(FlaskForm):
    survey_name = StringField("Name der Umfrage")
    submit_question = SubmitField("Frage hinzufügen")
    question_title = StringField("Fragentext")
    question_type = SelectField("Fragentyp", choices=[("rating", "rating"),
                                                          ("boolean", "boolean"), ("comment", "comment")],
                                validators=[DataRequired()])
    submit_survey = SubmitField("Umfrage final erstellen")
    create_survey = SubmitField("Umfrage anlegen")



