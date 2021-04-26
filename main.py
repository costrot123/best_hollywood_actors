from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
application = app


# Flask-WTF requires an encryption key - the key was changed in this repo for secuirity purposes
app.config['SECRET_KEY'] = 'Grt8y3Ve09TBRFbTP6jJ2D1NL0QDONRI'

# Flask-Bootstrap requires this line
Bootstrap(app)


def convert_to_dict(filename):
    datafile = open(filename, newline='')
    # create DictReader object
    my_reader = csv.DictReader(datafile)
    # create a regular Python list containing dicts
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts

actor_list = convert_to_dict('scrape_final.csv')

def get_names(source):
    names = []
    for row in source:
        # lowercase all the names for search feature
        name = row["name"].lower()
        names.append(name)
    return sorted(names)

def get_id(source, name):
    for row in source:
        if name.lower() == row["name"].lower():
            id = row["id"]
            id = str(id)
            # return id 
            return id

    return "Unknown"



class NameForm(FlaskForm):
    name = StringField("Please enter the actor's full name:", validators=[DataRequired()])
    submit = SubmitField('Search')


@app.route('/', methods=['GET', 'POST'])
def index():
    names = get_names(actor_list)
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        if name.lower() in names:
            form.name.data = ""
            num = get_id(actor_list, name)
            return redirect( url_for('actor', num=num) )
        else:
            message = "Actor is not in the databasa. Try searching for another actor!."

    return render_template('index.html', names=names, form=form, message=message, list=actor_list)


@app.route('/actor/<num>')
def actor(num):
    actor = actor_list[int(num) - 1]
    return render_template('actors.html', actor=actor)

@app.route('/list')
def list():
    return render_template('list.html', list=actor_list)




if __name__ == '__main__':
    app.run(debug=True)
