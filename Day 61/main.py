from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

app.secret_key = "ssecrety123"


@app.route("/")
def home():
    return render_template('index.html')


class MyForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password')
    submit = SubmitField(label='Submit')


@app.route("/login")
def login():
    form = MyForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
