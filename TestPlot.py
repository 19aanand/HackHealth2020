import pandas as pd
from bokeh.models import LabelSet
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components


testXValues = [1, 2, 3, 4, 5, 6, 7]
testYValues = [1, 2, 3, 4, 5, 6, 7]

plotTools = ["box_select", "hover", "reset"]
plot = figure(plot_width = 800, plot_height = 700, tools = plotTools)
plot.vbar(x = testXValues, top = testYValues, width = 0.75)
plot.y_range.start = 0


plot.xaxis.axis_label = "Day"
plot.yaxis.axis_label = "Total Steps"

script = components(plot)