from flask import Flask, render_template, request

# App creation
app = Flask(__name__)

# Feedback route
@app.route("/feedback", methods=["GET", "POST"])
def feed_back():
    if request.method == "POST":
        name = request.form.get("username")
        message = request.form.get("message")
        return render_template("thankyou.html", user=name, message=message)
    
    # GET request will render the feedback form
    return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True)
