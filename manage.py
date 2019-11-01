# manage.py

# from flask_script import Manager
# from project import app, db
# import unittest

# manager = Manager(app)

# @manager.command
# def recreate_db():
#     """Recreates a database."""
#     db.drop_all()
#     db.create_all()
#     db.session.commit()

# @manager.command
# def test():
#     """Runs the tests without code coverage."""
#     tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         return 0
#     return 1


# if __name__ == '__main__':
#     manager.run()


from flask import Flask
import time
from flask import Flask, render_template, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy


DBPATH = 'xc'
DBPASS = '123'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'testdb'


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '123'


db = SQLAlchemy(app)


class pathcount(db.Model):
    path = db.Column(db.String(100))
    count = db.Column('count', db.Integer, primary_key=True)

    def __init__(self, path, count):
        self.path = path
        self.count = count


def database_initialization_sequence():
    db.create_all()
    test_rec = pathcount(
        'A/D/CC',
        1)
    db.session.add(test_rec)
    db.session.rollback()
    db.session.commit()


app = Flask(__name__)


@app.route('/data', methods=['GET', 'POST'])
def getData():
    return "Some Data"


if __name__ == '__main__':
    dbstatus = False
    while dbstatus == False:
        try:
            db.create_all()
        except:
            time.sleep(2)
        else:
            dbstatus = True
    database_initialization_sequence()
    app.run(debug=True, host='0.0.0.0')
