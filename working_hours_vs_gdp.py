import gdp
import annual_working_hours_per_worker

dhours = annual_working_hours_per_worker.get()
dgdp = gdp.get()

x1,y1 = [],[]
for i in dhours:
    for b in dgdp:
        if i==b:
            x1.append(dhours[i])
            y1.append(dgdp[i])

from bokeh.plotting import figure,show
import numpy as np

f = figure()
for i in range(len(x1)):
    f.circle(x1[i],y1[i],size=10,color='blue')

x=np.array(x1)
y=np.array(y1)
par = np.polyfit(x, y, 1, full=True)
slope=par[0][0]
intercept=par[0][1]
y_predicted = [slope*i + intercept  for i in x]

f.line(x,y_predicted,color='red')

#labels
f.title = "Annual Working Hours vs Average GDP in Country"
f.xaxis.axis_label = "Average Annual Working Hours per Worker in Country"
f.yaxis.axis_label = "Average GDP of Country"

def get():
    global f
    return f