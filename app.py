from flask import Flask  , render_template,request,redirect,session,flash
import secrets
import sqlite3

app=Flask(__name__)
app.secret_key="123"

sqlconnection = sqlite3.connect("admin.db")
sqlconnection.execute("create table if not exists users(name text,password integer, email text)")
sqlconnection.close()



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        sqlconnection = sqlite3.connect('admin.db')
        sqlconnection.row_factory = sqlite3.Row
        cur = sqlconnection.cursor()

        cur.execute("SELECT * FROM users WHERE email = ? AND password = ?", ( email , password))
        data = cur.fetchone()
        if( data):
            session['email'] = data["email"]
            session['password'] = data["password"]
            return redirect("/courses")
        else:
            flash("Invalid email and Password", "danger")
            return redirect('/login')
    return render_template('login.html')


@app.route('/signup', methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        try:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            
            sqlconnection = sqlite3.connect('admin.db')

            cur = sqlconnection.cursor()
            cur.execute("INSERT INTO users(name, email, password) VALUES (?, ?, ?)", (name, email, password))
            
            sqlconnection.commit()
           
        except:
            flash("Error in Insert Operation", "danger")
        finally:
            sqlconnection.close()
            return redirect('/login')

    return render_template("signup.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/chat')
def chat():
    return render_template("chat.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/civil')
def civil():
    return render_template("civil.html")

@app.route('/college')
def college():
    return render_template("college.html")

@app.route('/college2')
def college2():
    return render_template("college2.html")

@app.route('/college3')
def college3():
    return render_template("college3.html")

@app.route('/college4')
def college4():
    return render_template("college4.html")

@app.route('/college5')
def college5():
    return render_template("college5.html")

@app.route('/college6')
def college6():
    return render_template("college6.html")

@app.route('/college7')
def college7():
    return render_template("college7.html")

@app.route('/college8')
def college8():
    return render_template("college8.html")

@app.route('/college9')
def college9():
    return render_template("college9.html")

@app.route('/college10')
def college10():
    return render_template("college10.html")

@app.route('/college11')
def college11():
    return render_template("college11.html")

@app.route('/college12')
def college12():
    return render_template("college12.html")

@app.route('/college13')
def college13():
    return render_template("college13.html")

@app.route('/college14')
def college14():
    return render_template("college14.html")

@app.route('/college15')
def college15():
    return render_template("college15.html")

@app.route('/college16')
def college16():
    return render_template("college16.html")

@app.route('/college17')
def college17():
    return render_template("college17.html")

@app.route('/college18')
def college18():
    return render_template("college18.html")

@app.route('/college19')
def college19():
    return render_template("college19.html")

@app.route('/college20')
def college20():
    return render_template("college20.html")

@app.route('/college21')
def college21():
    return render_template("college21.html")

@app.route('/college22')
def college22():
    return render_template("college22.html")

@app.route('/college23')
def college23():
    return render_template("college23.html")

@app.route('/college24')
def college24():
    return render_template("college24.html")

@app.route('/college25')
def college25():
    return render_template("college25.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

if __name__=="__main__":
    app.run(debug=True)