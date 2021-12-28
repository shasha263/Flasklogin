from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField, DateTimeField,DateField
from wtforms.validators import DataRequired,Email,EqualTo


class signupForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired()])
    email= StringField('Email',validators=[DataRequired(),Email()])    
    first_name= StringField('First Name',validators=[DataRequired()])
    last_name=StringField('Last Name',validators=[DataRequired()])
    password= PasswordField('Password',validators=[DataRequired()])
    confirm_password= PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    #date_created=DateField('Date Created',validators=[DataRequired()])
    submit=SubmitField()

class signinForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired()])
    password= PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField()

class updateUsernameForm(FlaskForm):
    newusername=StringField('New Username',validators=[DataRequired()])
    password= PasswordField('Password',validators=[DataRequired()])
    submit=SubmitField('Change Username')





