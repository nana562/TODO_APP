from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+ os.path.join(base_dir,"data.sqlite")
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

db=SQLAlchemy(app)

class TodoRecord(db.Model):
    __tablename__ = "todo_records"
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(40))

@app.route('/')
def index():
    records = TodoRecord.query.all()
    return render_template('home.html',
    records = records
    )

@app.route('/delete', methods=['POST'])
def delete():
  
    record = TodoRecord()
    db.session.delete(record)
    db.session.commit() 

    return redirect (url_for('index'))


@app.route('/save', methods=['POST'])
def save():
    saveFromUser = TodoRecord()
    saveFromUser.activity = request.form['activity']

    db.session.add(saveFromUser)
    db.session.commit()

    return redirect (url_for('index'))