from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import json
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///skilltest.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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


class AdminQuestionForm(FlaskForm):
    exam_id = StringField(label='ExamID')
    exam_name = StringField(label='Exam Name')
    question = StringField(label='Question')
    option_1 = StringField(label='Option_1')
    option_2 = StringField(label='Option_2')
    option_3 = StringField(label='Option_3')
    option_4 = StringField(label='Option_4')
    answer = StringField(label='Answer')
    submit = SubmitField(label='Add')



##CREATE TABLE
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(250), unique=True, nullable=False)
    exam_1 = db.Column(db.String(250), nullable=True)
    exam_2 = db.Column(db.String(250), nullable=True)
    exam_3 = db.Column(db.String(250), nullable=True)
    exam_4 = db.Column(db.String(250), nullable=True)
    password = db.Column(db.String(250), nullable=False)


class Question(db.Model):
    exam_id = db.Column(db.Integer, nullable=False)
    exam_name = db.Column(db.String(250), nullable=False)
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(250), nullable=False)
    option_1 = db.Column(db.String(250), nullable=True)
    option_2 = db.Column(db.String(250), nullable=True)
    option_3 = db.Column(db.String(250), nullable=True)
    option_4 = db.Column(db.String(250), nullable=True)
    answer = db.Column(db.String(250), nullable=False)
db.create_all()

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


# @app.route('/admin_adduser',methods=["POST","GET"])
# def admin_adduser():
#     admin_userform = AdminUserForm()
#     if admin_userform.is_submitted():
#         user = admin_userform.user.data
#         password = admin_userform.password.data
#         user_dict = {user: {'password':password}}
#         try:
#             with open('db/users.json', 'r') as users_file:
#                 data = json.load(users_file)
#                 data.update(user_dict)
#         except:
#             with open('db/users.json', 'w') as users_file:
#                 json.dump(user_dict, users_file)
#             return 'in except-user added'
#         else:
#             with open('db/users.json', 'w') as users_file:
#                 json.dump(data, users_file)
#             return 'in else-user added'
#     else:
#         return render_template('admin-add_user.html', form=admin_userform)


@app.route('/admin_adduser',methods=["POST","GET"])
def admin_adduser():
    admin_userform = AdminUserForm()
    if admin_userform.is_submitted():
        user = admin_userform.user.data
        password = admin_userform.password.data
        new_user = User(user_name=user, password=password)
        db.session.add(new_user)
        db.session.commit()
        return 'user_added'
    else:
        return render_template('admin-add_user.html', form=admin_userform)


@app.route('/admin_addquestion',methods=["POST","GET"])
def admin_addquestion():
    admin_questionform = AdminQuestionForm()
    if admin_questionform.is_submitted():
        exam_id = int(admin_questionform.exam_id.data)
        exam_name = admin_questionform.exam_name.data
        question = admin_questionform.question.data
        option_1 = admin_questionform.option_1.data
        option_2 = admin_questionform.option_2.data
        option_3 = admin_questionform.option_3.data
        option_4 = admin_questionform.option_4.data
        answer = admin_questionform.answer.data
        new_question = Question(exam_id=exam_id, exam_name=exam_name, question=question
                            , option_1=option_1, option_2=option_2, option_3=option_3, option_4=option_4, answer=answer)
        db.session.add(new_question)
        db.session.commit()
        return render_template('admin_addquestion.html', form=admin_questionform)
    else:
        return render_template('admin_addquestion.html', form=admin_questionform)


if __name__ == '__main__':
    app.run(debug=True)
