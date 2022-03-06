from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import json
app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

class LoginForm(FlaskForm):
    user = StringField(label='User')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Log In')


class AdminForm(FlaskForm):
    user = StringField(label='User')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Log In')


class AdminUserForm(FlaskForm):
    user = StringField(label='User')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Add')


@app.route('/home', methods=["GET", "POST"])
def home():
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.is_submitted():
            user = login_form.user.data
            return render_template('login_home.html', user=user)
    else:  # You only want to print the errors since fail on validate
        return render_template('home.html', form=login_form)


@app.route('/home/loginsuccess',methods=["POST"])
def login_home():
    return 'success'

@app.route('/admin',methods=["GET","POST"])
def admin():
    admin_form = AdminForm()
    if request.method == 'POST':
        if admin_form.is_submitted():
            user = admin_form.user.data
            password = admin_form.password.data
            if user == 'admin' and password == 'test':
                return render_template('admin_home.html', user=user)
            else:
                return 'login failed'
    else:  # You only want to print the errors since fail on validate
        return render_template('admin.html', form=admin_form)


@app.route('/admin_adduser',methods=["POST","GET"])
def admin_adduser():
    admin_userform = AdminUserForm()
    if admin_userform.is_submitted():
        user = admin_userform.user.data
        password = admin_userform.password.data
        user_dict = {'users':{"user":user, "password":password}}
        try:
            with open('db/users.json', 'r') as users_file:
                data = json.load(users_file)
                # data.update(user_dict)
        except:
            with open('db/users.json', 'w') as users_file:
                json.dump(user_dict, users_file)
                return 'user added'
        else:
            with open('db/users.json', 'w') as users_file:
                json.dump(data, users_file)
            return 'user added'
    else:
        return render_template('admin-add_user.html', form=admin_userform)

if __name__ == '__main__':
    app.run(debug=True)
