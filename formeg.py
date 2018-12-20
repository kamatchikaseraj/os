from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class InfoForm(FlaskForm):

    name = StringField('Enter the name.')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = False
    form = InfoForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('display.html', form=form, name=name)


if __name__ == '__main__':
    app.run(debug=True)
