from flask import Flask,render_template,Response
from flask_cors import CORS,cross_origin

from app.home.home import home_blueprint



app=Flask(__name__)
app.config['SECRET_KEY']='&X\x10\xd0\x02\x19\xaa9\x14+j\xea\x97\xadj\xe0\xc1\x18\x9a\xb7#\xf0\x84?\x81\xea'
app.config['CORS_HEADERS'] = 'application/json'
cors=CORS(app)

@app.route('/',methods=['GET','POST'])
def first_point():
    
    return render_template('registration.html')





app.register_blueprint(home_blueprint)
