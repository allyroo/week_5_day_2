#capital in Blueprint indicates that we are working with a class
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import User, db
from forms import UserLoginForm

auth = Blueprint('auth',__name__, template_folder ='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
# get gets data from our database, post means they can post on page; methods work universally
# GET/POST/PUT/DELETE are HTTP verbs that describe what we want to do at a given endpoint (location)
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email,password)

            user = User(email, password = password)

            db.session.add(user)
            db.session.commit()


            flash(f'You have successfully created  user account {email}', 'User-created')
    
            return redirect(url_for('site.home'))


    except:
        raise Exception('Invalid Form Data: Please Check your Form')
    return render_template('signup.html', form=form)
    

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    return render_template('signin.html')