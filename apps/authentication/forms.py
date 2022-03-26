# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

#import pwd
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, IntegerField, DecimalField, MultipleFileField
from wtforms.validators import Email, DataRequired
import sqlite3

# login and registration


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])

class ProfileForm(FlaskForm):
    firstname = StringField('firstname',id='firstname',validators=[DataRequired()])
    lastname = StringField('lastname',id='lastname',validators=[DataRequired()])
    birthday = DateField('bday',id='bday',validators=[DataRequired()])
    gender = SelectField('sex',id='sex',choices=['Male', 'Female'])
    address = StringField('address',id='address',validators=[DataRequired()])
    apt_no = StringField('apt_no',id='apt_no',validators=[DataRequired()])
    city = StringField('city',id='city',validators=[DataRequired()])
    state = SelectField('state', id='state', choices=[])
    pincode = IntegerField('pin', id='pin', validators=[DataRequired()])
    yearofstudy = IntegerField('yos', id='yos', validators=[DataRequired()])
    Marks = DecimalField('yos', id='yos', validators=[DataRequired()])
    institute = StringField('ins',id='ins',validators=[DataRequired()])
    account = IntegerField('account', id='account', validators=[DataRequired()])
    ifsc = StringField('ifsc',id='ifsc',validators=[DataRequired()])
    branch = StringField('branch',id='branch',validators=[DataRequired()])
    edu = MultipleFileField('edu', id='edu', validators=[DataRequired()]) 
    pwds = MultipleFileField('pwds', id='pwds', validators=[DataRequired()])
    income = MultipleFileField('inc', id='inc', validators=[DataRequired()])
    addr = MultipleFileField('addr', id='addr', validators=[DataRequired()])
