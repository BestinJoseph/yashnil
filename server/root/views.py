from flask import Blueprint, render_template, url_for, redirect

root_blueprint = Blueprint('root_blueprint', __name__)

@root_blueprint.route('/')
def root_home() :
    houses=[]
    return render_template('root_home.html', houses=houses)