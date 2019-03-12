from flask import Blueprint,render_template,request,redirect

from app.classes.Offers import Offers
from app.classes.Registration import Registration
home_blueprint=Blueprint('home',__name__,template_folder='templates',static_folder='static')


@home_blueprint.route('/offers',methods=['GET','POST'])
def get_offers():
    of=Offers()
    data=of.get_offers()
    
    return render_template('offers.html',offers=data)


@home_blueprint.route('/registration',methods=['GET','POST'])
def registration():
    name=request.args.get('name')
    number=request.args.get('number')
    re=Registration()
    re.set_name(name)
    re.set_number(number)
    re.save_resgistration()
    return redirect('/offers')


    