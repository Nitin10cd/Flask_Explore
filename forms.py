from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  SubmitField
from wtforms.validators import DataRequired , Email, Length

# ADDING THE FORM WTF PACKAGE OF THE FLASK

#making the class 
class RegistrationForm(FlaskForm):

    # making the props and the field vlaues adding the validatrs
    name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password" ,validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")

    
