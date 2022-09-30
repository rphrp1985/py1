from flask import Flask , jsonify


appFlask = Flask(__name__)
@appFlask.route('/<string:name>')
def home(name):
    name= name.lower()
    if name== 'priyanka':
        return 'Prianshu Loves You'
    else:
        return 'Prianshu Does Not Love You'



if __name__ == "__main__":
  appFlask.run(debug=True)



if __name__=='__main__':
    appFlask.run(debug=True)


