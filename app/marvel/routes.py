from flask import Blueprint,render_template,request,redirect,url_for,flash
from app.forms import signupForm,signinForm,updateUsernameForm

from app.models import db,User
from flask_login import login_user,logout_user,current_user,login_required
from werkzeug.security import check_password_hash


marvel= Blueprint('marvel',__name__,template_folder='marvel_templates',url_prefix='/marvel')

@marvel.route('/signin',  methods=['GET','POST'])
def signin():
    form=signinForm()
    if request.method=='POST':
        if form.validate_on_submit():
            print('Congratulation!!! Correct User Info')
            print(form.username.data,form.password.data)
            user=User.query.filter_by(username=form.username.data).first()  
            if user is None or not check_password_hash(user.password, form.password.data):
                flash('Username or Password did not match!!!',category='danger')
                return redirect(url_for('marvel.signin'))
            login_user(user)
            print(current_user,current_user.__dict__)

            flash(f'Thanks for logging in, {user.username}.',category='info')
            return redirect(url_for('home'))          

        else:
            flash('Invalid Input, try again', category='warning')
            return redirect(url_for('marvel.signin'))

    return render_template('signin.html',form=form)

@marvel.route('/register', methods=['GET','POST'])
def signup():
    form=signupForm()
    if request.method=='POST':
        if form.validate_on_submit():
            print('Congratulation!!! Correct User Info')
            new_user=User(form.username.data,form.email.data,form.first_name.data,form.last_name.data,form.password.data)
            print(f'New user created- {new_user.__dict__}')
            try:
                db.session.add(new_user)
                db.session.commit()
            except:
                flash('Username or email alreday taken',category='warning')
                return redirect(url_for('marvel.signup'))
            
            login_user(new_user)
            flash(f'Thank you for signing up {new_user.first_name} {new_user.last_name}',category='info')
            return redirect(url_for('home'))

        else:
            flash('Invalid Input, try again',category='warning')
            return redirect(url_for('marvel.signup'))

    return render_template('signup.html',form=form)

@marvel.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.',category='info')
    return redirect(url_for('marvel.signin'))



@marvel.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    form=updateUsernameForm()
    if request.method=='POST':
        if form.validate_on_submit() and check_password_hash(current_user.password,form.password.data):
            if User.query.filter_by(username=form.newusername.data).first():
                flash('Username already taken, Please try a different one.',category='danger')
                return redirect(url_for('marvel.profile'))
            else:
                current_user.username=form.newusername.data
                db.session.commit()
                flash('Your username has been updated!', category='success')
                return redirect(url_for('marvel.profile'))

            
        else:
            flash('Incorrect password,try again',category='danger')
            return redirect(url_for('marvel.profile'))

    return render_template('profile.html',form=form)


    

    
