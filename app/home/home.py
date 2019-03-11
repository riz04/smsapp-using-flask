from flask import Blueprint,render_template


home_blueprint=Blueprint('home',__name__,template_folder='templates',static_folder='static')


@home_blueprint.route('/offers',methods=['GET','POST'])
def get_offers():
    