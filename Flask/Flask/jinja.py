### Jinja2 Template Engine --> 
'''
{{   }} --> expressions to print output in html
{%...%} --> conditions, for loops
{#...#} --> comments
'''

from flask import Flask,render_template,request
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
## WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

## Variable Rule
@app.route('/success/<score>')
def success(score):
    return "The marks you got is "+ score

@app.route('/intsuccess/<int:score>')
def success1(score):
    return "The marks you got is "+ str(score)

## Jinja2 Template Engine
@app.route('/dynamic/<int:score>')
def dynamic(score):
    res = ""
    if(score > 50):
        res = "PASSED"
    else:
        res = "FAILED"
    
    return render_template('result.html', res = res) ## There is no compulsion on the attribute name
    
@app.route('/dynamic_res/<int:score>')
def dynamic1(score):
    res = ""
    if(score > 50):
        res = "PASSED"
    else:
        res = "FAILED"
        
    exp = {'score' : score, 'res' : res}
    
    return render_template('result1.html', res = exp)
  
## For if condition in HTML
@app.route('/dynamic_res_if/<int:score>')
def dynamic2(score):
    
    return render_template('result2.html', result = score)
  
if __name__=="__main__":
    app.run(debug=True)