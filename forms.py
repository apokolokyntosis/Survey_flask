from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CreateSurveyForm(FlaskForm):
    survey_name = StringField("Survey name")
    submit_question = SubmitField("Add question")
    question_title = StringField("Question")
    question_type = SelectField("Question type", choices=[("rating", "rating"),
                                                          ("boolean", "boolean"), ("comment", "comment")],
                                validators=[DataRequired()])
    submit_survey = SubmitField("Create Survey")


