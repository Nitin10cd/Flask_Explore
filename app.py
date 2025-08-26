from flask import Flask, render_template, redirect, request, url_for, flash
#importig the form created in wtf 
from forms import RegistrationForm

# App creation
app = Flask(__name__)
# Secret key for flash messages
app.secret_key = "my_secret"

@app.route("/", methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome, {name}! You Registered Successfully", "Success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

# route for the success
@app.route("/success")
def success():
    return render_template("success.html")



# @app.route("/", methods=["GET", "POST"])
# def form():
#     if request.method == "POST":
#         name = request.form.get("name")
#         message = request.form.get("message")

#         # Error handling
#         if not name:
#             flash("Name cannot be empty", "error")
#             return redirect(url_for("form"))
#         if not message:
#             flash("Message cannot be empty", "error")
#             return redirect(url_for("form"))

#         # Render thank-you page with user info
#         return redirect("thankyou.html", user=name, message=message)

#     return render_template("form.html")
 


# @app.route("/thankyou")
# def thankyou():
#     return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)



