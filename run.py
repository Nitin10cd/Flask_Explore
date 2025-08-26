#basically a runner file which creates the instance of the app 
from app import create_app
app = create_app()

# run only when it run
if __name__ == "__main__":
    app.run(debug=True)