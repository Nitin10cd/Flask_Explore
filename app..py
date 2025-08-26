# ADVANCE FORM HANDLING IN THE PYTHON 
# => Using the req.form in flask

from flask import Flask, render_template, request

# app creation 
app = Flask(__name__)

# feedback shareing route dynamic
@app.route("/feedback", methods = ["POST", "GET"])
def feed_back():
    if request.method == "POST":
        name = request.form.get("username")
        message = request.form.get("message")

        return render_template("thankyou.html", user = name, message = message)

if __name__ == "__main__":
    app.run(debug=True)





