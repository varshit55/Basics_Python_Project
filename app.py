from flask import Flask



app=Flask(__name__)




@app.route('/home')
def hello():
    return "hello everyone this our first flask web application"

@app.route('/hyderabad') 
def he():
    return "hello everyone this our first flask web application second"


if __name__=='__main__':

      
    app.run(debug=True)