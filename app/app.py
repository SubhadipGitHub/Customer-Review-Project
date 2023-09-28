from flask import Flask, render_template, request, url_for,redirect
from collections import defaultdict
from wtforms import Form,TextField,TextAreaField,validators,StringField,SubmitField
import csv

app = Flask(__name__)

class ReviewForm(Form):
    fname = TextField('First Name *', validators=[validators.DataRequired()])
    pname = TextField('Product *', validators=[validators.DataRequired()])
    review = TextField('Review *', validators=[validators.DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def home():
    columns = defaultdict(list)  # each value in each column is appended to a list
    with open('data.csv') as f:
        reader = csv.DictReader(f)  # read rows into a dictionary format
        for row in reader:  # read a row as {column1: value1, column2: value2,...}
            for (k, v) in row.items():  # go over each column name and value
                columns[k].append(v)  # append the value into the appropriate list
                # based on column name k

    if request.method == 'post':
        #dO SOMETHING
        userdata = dict(request.form)
        print(userdata)
        with open('data.csv', mode='a') as csv_file:
            data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data.writerow([userdata.get('fname'), userdata.get('pname'), userdata.get('reviews')])
    return render_template('index.html',form=ReviewForm, results = columns)

@app.route("/submit", methods=["GET", "POST"])
def submit():
  if request.method == "GET":
    return redirect(url_for('home'))
  elif request.method == "POST":
      userdata = dict(request.form)
      print(userdata)
      with open('data.csv', mode='a') as csv_file:
          data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
          data.writerow([userdata.get('fname'), userdata.get('pname'), userdata.get('reviews')])
  return "Review added!"

if __name__ == '__main__':
   app.run()
