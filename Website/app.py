from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/EmpMan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Cord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x_cord = db.Column(db.Integer)
    y_cord = db.Column(db.Integer)

    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord


@app.route('/', methods=['GET', 'POST'])
def index():
   '''x_cord = request.form['xs_cord']
    y_cord = request.form['ys_cord']

    my_data =Cord(x_cord, y_cord)

    db.session.add(my_data)
    db.session.commit()'''


    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)