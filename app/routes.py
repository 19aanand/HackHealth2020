import pandas as pd
from bokeh.models import LabelSet
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from app import app
from flask import render_template

#@app.route('/')
#@app.route('/')
#def index(script):
 # return render_template(script[1] + script[2])


@app.route('/')
@app.route('/index')
def index():
  app.run(debug=True)
  return render_template('Homepage.html', code=code)
