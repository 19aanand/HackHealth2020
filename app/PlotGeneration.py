import pandas as pd
from bokeh.models import LabelSet
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components

def Replace(str1): 
    str1 = str1.replace(',', 'third') 
    str1 = str1.replace('.', '') 
    str1 = str1.replace('third', '.') 
    return str1
  
  
  
def returnCode():

    reader= pd.read_csv('One_Year_of_FitBitChargeHR_Data.csv', ',', names = ['Date', 'Calories', 'Steps', 'Distance', 'floors',
                                                                              'Minutes_sitting', 'Minutes_of_slow_activity',
                                                                              'Minutes_of_moderate_activity', 
                                                                              'Minutes_of_intense_activity', 'Calories_Activity'])

    a = "5788"
    b = int(a)
    print(b)

    i = 1
    xValues = [1, 2, 3, 4, 5, 6, 7]
    yValues = []

    while i <= 7:
        y = reader['Steps'][i]
        y = int(Replace(y))
        yValues.append(y)
        i+=1



    output_file("StepsTracked.html")

    plotTools = ["box_select", "hover", "reset"]
    plot = figure(plot_width = 800, plot_height = 700, tools = plotTools)
    plot.vbar(x = xValues, top = yValues, width = 0.75)
    plot.y_range.start = 0


    plot.xaxis.axis_label = "Day"
    plot.yaxis.axis_label = "Total Steps"

    script = components(plot)

    return script[1] + script[0]
