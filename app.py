from flask import Flask , jsonify



appFlask = Flask(__name__)

@appFlask.route('/',methods=['GET'])
def index():
    return 'Wrong entry'





@appFlask.route('/<string:name>',methods=['GET'])
def home(name):
    name= name.lower()
    if name== 'priyanka':
        return 'Prianshu Loves You'
    else:
        return 'Prianshu Does Not Love You'



if __name__ == "__main__":
  appFlask.run(debug=False)


