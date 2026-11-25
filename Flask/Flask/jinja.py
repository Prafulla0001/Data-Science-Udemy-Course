# ### Jinja2 Template Engine --> 
# '''
# {{   }} --> expressions to print output in html
# {%...%} --> conditions, for loops
# {#...#} --> comments
# '''

# from flask import Flask,render_template,request,redirect,url_for
# '''
#  It creates an instance of the Flask class, 
#  which will be your WSGI (Web Server Gateway Interface) application.
# '''
# ## WSGI Application
# app=Flask(__name__)

# @app.route("/")
# def welcome():
#     return "<html><H1>Welcome to the flask course</H1></html>"

# @app.route("/index",methods=['GET'])
# def index():
#     return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/form',methods=['GET','POST'])
# def form():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello {name}!'
#     return render_template('form.html')

# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello {name}!'
#     return render_template('form.html')

# ## Variable Rule
# @app.route('/success/<score>')
# def success(score):
#     return "The marks you got is "+ score

# @app.route('/intsuccess/<int:score>')
# def success1(score):
#     return "The marks you got is "+ str(score)

# ## Jinja2 Template Engine
# @app.route('/dynamic/<int:score>')
# def dynamic(score):
#     res = ""
#     if(score > 50):
#         res = "PASSED"
#     else:
#         res = "FAILED"
    
#     return render_template('result.html', res = res) ## There is no compulsion on the attribute name
    
# @app.route('/dynamic_res/<int:score>')
# def dynamic1(score):
#     res = ""
#     if(score > 50):
#         res = "PASSED"
#     else:
#         res = "FAILED"
        
#     exp = {'score' : score, 'res' : res}
    
#     return render_template('result1.html', res = exp)
  
# ## For if condition in HTML
# @app.route('/dynamic_res_if/<int:score>')
# def dynamic2(score):
    
#     return render_template('result2.html', result = score)
  
# ## Dynamic url for Fail
# @app.route('/dyanmic_fail/<int:score>')
# def dynamic3(score):
    
#     return render_template('result2.html', result = score)

# @app.route('/submit1', methods=['POST'])
# def submit1():

#     science = float(request.form['science'])
#     maths = float(request.form['maths'])
#     c = float(request.form['c'])
#     data_science = float(request.form['datascience'])

#     print("Science:", science)
#     print("Maths:", maths)
#     print("C:", c)
#     print("Data Science:", data_science)

#     total_score = (science + maths + c + data_science) / 4

#     print("Total Score:", total_score)

#     return redirect(url_for('dynamic2', score=int(total_score)))
    
# if __name__=="__main__":
#     app.run(debug=True)

### -----------------------------------------------------------------------------------------------------------------------------

### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine

### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
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

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    return render_template('result.html',results=res)

## Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score':score,"res":res}

    return render_template('result1.html',results=exp)

## if confition
@app.route('/sucessif/<int:score>')
def successif(score):

    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))

if __name__=="__main__":
    app.run(debug=True)
