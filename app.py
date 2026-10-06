from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)
@app.route('/')
def welcome():
    return "welcome to flaskapp<==>routing"
@app.route('/greet/<uname>')
def greet(uname):
    return f"Good Morning,{uname}!"



@app.route('\calculate', methods=['GET','POST'])
def Si():
    if request.method=='POST':
        P=float(request.form['p'])
        T=float(request.form['t'])
        R=float(request.form['r'])
        result=(P*T*R)/100
        total=P+result
        return render_template('index.html', result=result,total=total,p=P,t=T,r=R)
    return render_template('index.html')
   


if __name__=='__main__':
    app.run(debug=True,port=3500)