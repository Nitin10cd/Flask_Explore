from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"

# Home / Login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username  # store in session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid Credentials, Try Again", mimetype="text/plain")
    
    # Login form
    return '''
        <h2>Login Page</h2>
        <form method="POST"> 
            Username: <input type="text" name="username" /> <br/>
            Password: <input type="password" name="password" /> <br/>
            <input type="submit" value="Login" />
        </form>
    '''

# Welcome page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome, {session["user"]}!</h2>
            <a href="{url_for('logout')}">Logout</a>
        '''
    return redirect(url_for("login"))

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask,request

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"

# @app.route("/about")
# def about():
#     return "You are in abt page"

# @app.route("/contact")
# def contact():
#     return "you are in contact page"

# # making the req with the types
# @app.route("/submit", methods = ["GET", "POST"])
# def submit():
#     if request.method == "POST":
#         return "You Have Sent The Dta"
#     else:
#         return "You have recived the data"


# if __name__ == "__main__":
#     app.run(debug=True)
