from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField

app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class InfoForm(FlaskForm):

    name = StringField('Enter the name.')
    num1 = IntegerField('Number1')
    num2 = IntegerField('Number2')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = False
    form = InfoForm()
    sum=0
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        n1 = form.num1.data
        n2 = form.num2.data
        sum = n1+n2
        print sum
    return render_template('display.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
