from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

DBUSER = 'postgres'
DBPASS = 'postgres'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'path_count'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'postgres'

db = SQLAlchemy(app)


class pathcount(db.Model):
    path = db.Column(db.String(100), primary_key=True)
    count = db.Column(db.Integer)

    def __init__(self, path, count):
        self.path = path
        self.count = count


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<path:dummy>')
def fallback(dummy):
    # catch everything else here
    record = pathcount.query.filter_by(path=dummy).first()
    if(record is None):
      record = pathcount(dummy,1)
      db.session.add(record)
    else:
      record.count = record.count + 1
    db.session.commit()
    return render_template('showPath.html', pathcount=pathcount.query.order_by(pathcount.path))


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')
