"""
routes.py
"""
from flask import Blueprint, render_template, request
from app.ml.model import create_model
from app.ml.predict import make_prediction

main = Blueprint('main', __name__)
model = create_model()
@main.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        qb_p = float(request.form['qb_percentage'])
        offense_p = float(request.form['offense_percentage'])
        defense_p = float(request.form['defense_percentage'])

        prediction = make_prediction(model, qb_p, offense_p, defense_p)

    return render_template('index.html', prediction=prediction)

