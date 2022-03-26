# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.headerregistry import Address
from types import CoroutineType
import sqlite3 as sql
import markupsafe
from apps import db
from apps.home import app, blueprint
from flask import render_template, request, redirect
from flask_login import login_required
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename
from apps.authentication.forms import ProfileForm
from apps.authentication.models import Users
import os 


app.config["UPLOAD_FOLDER"] = "/static/docs/"


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')

@blueprint.route('/settings', methods= ["GET", "POST"])
def profile():
    profile_form = ProfileForm(request.form)
    profile = Users(**request.form)

    print(profile)
    db.session.add(profile)
    db.session.commit()
    
    return render_template('home/settings.html', form=profile_form)

@blueprint.route('/add',methods=['GET','POST'])
def add():
    print('DONE')
    
    conn=sql.connect('apps/site.db')
    cur=conn.cursor()

    if request.method == 'POST':
        firstname = request.form['first_name']
        lastname = request.form['last_name']
        birthday = request.form['birthday']
        gender = request.form['gender']
        address = request.form['address']
        apt_no = request.form['number']
        city = request.form['city']
        state = request.form['state']
        pincode = request.form['zip']
        yearofstudy = request.form['yos']
        marks = request.form['mip']
        institute = request.form['ins']
        account = request.form['account']
        ifsc = request.form['ifsc']
        branch = request.form['branch']
        print('DONE')
        
        cur.execute("""INSERT INTO SubmitClaim (type, receipt, amount, description) VALUES (?, ?, ?, ?)""", 
                    (firstname, lastname, birthday, gender, address, apt_no, city, state,
                     pincode, yearofstudy, marks, institute, account, ifsc, branch))
        conn.commit()
        conn.close()
        print('DONE')

    return render_template('home/settings.html')
    
@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# @blueprint.route('/settings', methods= ["GET", "POST"])
# @login_required
# def profile():
#     profile_form = ProfileForm(request.form)
#     # if request.method == 'POST':
#     #     f = request.files['file']
#     #     filename = secure_filename(f.filename)
#     #     f.save(os.path.join(app.config['UPLOAD_FOLDER'] , f.filename))    
#     #     file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
#     #     content = file.read()   
#     #     flash("file uploaded successfully")
#     # return render_template('settings.html', filename=filename)

#     if 'settings' in request.form:
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         birthday = request.form['birthday']
#         gender = request.form['gender']
#         address = request.form['address']
#         apt_no = request.form['apt_no']
#         city = request.form['city']
#         state = request.form['state']
#         pincode= request.form['pincode']
#         yearofstudy= request.form['yearofstudy']
#         Marks= request.form['Marks']
#         institute= request.form['institute']
#         account= request.form['account']
#         ifsc= request.form['ifsc']
#         branch= request.form['branch']

#     user = Users(**request.form)
#     db.session.add(user)
#     db.session.commit()




# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
