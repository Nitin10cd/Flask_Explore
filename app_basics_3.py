from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def student_profile():
    return render_template(
        "profile.html",  
        name="Arun",
        is_topper=True,
        subjects=["MATHS", "Sci"]
    )

if __name__ == "__main__":
    app.run(debug=True)
