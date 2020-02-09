from flask import Flask, render_template
import PlotGeneration

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    code = PlotGeneration.returnCode()
    print(code)
    return render_template("Homepage.html", code=code)
    
if __name__ == '__main__':
    app.run(debug=True)