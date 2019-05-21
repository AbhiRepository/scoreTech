from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField


roles = ['Student', 'Teacher', 'Admin']

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	phone = StringField('Phone number', validators=[DataRequired(), Length(min=10, max=10)])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	schoolId = StringField('School ID', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class OTPForm(FlaskForm):
	OTP = StringField('OTP', validators=[DataRequired(), Length(min=6, max=6)])
	submit = SubmitField('Verify')

class CreateUserForm(FlaskForm):
	firstname = StringField('First Name', validators=[DataRequired()])
	secondname = StringField('Second Name')
	schoolId = StringField('School ID', validators=[DataRequired()])
	options = StringField('Role', validators=[DataRequired()])
	submit = SubmitField('Create User')

class ForgotForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Send verification email')
		

class ResetForm(FlaskForm):
	code = StringField('Code', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Reset password')