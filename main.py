from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def homepage():
#     return render_template("index.html")

@app.route('/')
def homepage():
    movies = ["Mroczny zakatek", "Amelia", "Gwiezdny pyl"]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)