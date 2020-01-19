from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class CreateSurveyForm(FlaskForm):
    survey_name = StringField("Survey name", validators=[DataRequired()])
    submit = SubmitField("Create survey")
    question_title = StringField("Question", validators=[DataRequired()])
    question_type = StringField("Question type", validators=[DataRequired()])


