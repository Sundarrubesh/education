from flask import Flask  , render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/blog.html')
def blog():
    return render_template("blog.html")

@app.route('/civil.html')
def civil():
    return render_template("civil.html")

@app.route('/college.html')
def college():
    return render_template("college.html")

@app.route('/college2.html')
def college2():
    return render_template("college2.html")

@app.route('/college3.html')
def college3():
    return render_template("college3.html")

@app.route('/college4.html')
def college4():
    return render_template("college4.html")

@app.route('/college5.html')
def college5():
    return render_template("college5.html")

@app.route('/college6.html')
def college6():
    return render_template("college6.html")

@app.route('/college7.html')
def college7():
    return render_template("college7.html")

@app.route('/college8.html')
def college8():
    return render_template("college8.html")

@app.route('/college9.html')
def college9():
    return render_template("college9.html")

@app.route('/college10.html')
def college10():
    return render_template("college10.html")

@app.route('/college11.html')
def college11():
    return render_template("college11.html")

@app.route('/college12.html')
def college12():
    return render_template("college12.html")

@app.route('/college13.html')
def college13():
    return render_template("college13.html")

@app.route('/college14.html')
def college14():
    return render_template("college14.html")

@app.route('/college15.html')
def college15():
    return render_template("college15.html")

@app.route('/college16.html')
def college16():
    return render_template("college16.html")

@app.route('/college17.html')
def college17():
    return render_template("college17.html")

@app.route('/college18.html')
def college18():
    return render_template("college18.html")

@app.route('/college19.html')
def college19():
    return render_template("college19.html")

@app.route('/college20.html')
def college20():
    return render_template("college20.html")

@app.route('/college21.html')
def college21():
    return render_template("college21.html")

@app.route('/college22.html')
def college22():
    return render_template("college22.html")

@app.route('/college23.html')
def college23():
    return render_template("college23.html")

@app.route('/college24.html')
def college24():
    return render_template("college24.html")

@app.route('/college25.html')
def college25():
    return render_template("college25.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/signup.html')
def signup():
    return render_template("signup.html")

if __name__=="__main__":
    app.run(debug=True)