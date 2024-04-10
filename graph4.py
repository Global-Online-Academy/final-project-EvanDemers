import world_happiness
import gdp

d1,d2 = world_happiness.get(),gdp.get()

x1,y1 = [],[]
for i in d1:
    for c in d2:
        if i==c:
            x1.append(d1[i])
            y1.append(d2[i])

from bokeh.plotting import figure
import numpy as np

f=figure()
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
f.title = "General Happiness vs Average GDP per Country"
f.xaxis.axis_label = "General Happiness of Country (0-10)"
f.yaxis.axis_label = "Average GDP of Country"

def get():
    global f
    return f