from flask import Flask, render_template, request

app = Flask(__name__)

# route for the main
@app.route("/")
def login():
    return render_template("login.html")
# rendering the html page using the flask render_html
#using jinja template also in next target

# making the submit route for the html form
@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    
    #currently not adding the logic for the any pass match that thing i already know
    # if username == "nitin123" and password == "pass":
    #     return render_template("home.html", name=username)
    # NOW FOR THE MORE THAN ONE USERS AS WE NOT USING THE DB JUST I USE THE DICTIONARY

    valid_users = {
        'admin': '123',
        'nitin123': 'pass',
        'someonespecial': 'damn'
    }
    #using the dict and the membership operators
    if username in valid_users and password == valid_users[username]:
        return render_template("home.html",name = username)
    else:
        # fixed: cannot return html inside python like earlier
        return "Invalid Credentials"


