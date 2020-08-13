from flask import Blueprint, render_template, url_for, redirect

house_blueprint = Blueprint('house_blueprint', __name__, url_prefix="/houses")

@house_blueprint.route('/')
def house_home() :
    houses = []
    return render_template('house_home.html', houses=houses)

@house_blueprint.route('/<int:house_id>')
def house_single(house_id) :
    house = {}
    return render_template('house_single.html', house=house)