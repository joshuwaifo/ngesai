from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[Length(max=64)])
    last_name = StringField('Last Name', validators=[Length(max=64)])
    organization = StringField('Organization', validators=[Length(max=128)])
    role = SelectField('Role', choices=[
        ('', 'Select your role'),
        ('government', 'Government Entity'),
        ('investor', 'Investor'),
        ('developer', 'Game Developer'),
        ('esports_team', 'Esports Team/Organization'),
        ('player', 'Player/Coach'),
        ('content_creator', 'Content Creator'),
        ('event_organizer', 'Event Organizer'),
        ('educator', 'Educator'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    language_preference = SelectField('Language Preference', choices=[
        ('en', 'English'),
        ('ar', 'Arabic')
    ], default='en')
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class QueryForm(FlaskForm):
    query_text = TextAreaField('Enter your question or request', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Submit')

class ReportForm(FlaskForm):
    title = StringField('Report Title', validators=[DataRequired(), Length(min=5, max=120)])
    category = SelectField('Report Category', choices=[
        ('market_analysis', 'Market Analysis'),
        ('investment_proposal', 'Investment Proposal'),
        ('sponsorship_package', 'Sponsorship Package'),
        ('performance_dashboard', 'Performance Dashboard'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    description = TextAreaField('Report Description', validators=[DataRequired(), Length(min=20, max=1000)])
    submit = SubmitField('Generate Report')

class SearchForm(FlaskForm):
    search_query = StringField('Search Query', validators=[DataRequired(), Length(min=3, max=100)])
    submit = SubmitField('Search')
