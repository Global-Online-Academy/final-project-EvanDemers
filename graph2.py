from bokeh.plotting import figure
import numpy as np

import productivity_n_hourly_compensation

prod,comp = productivity_n_hourly_compensation.get()

f = figure()
for i in range(len(prod)):
    f.circle(prod[i],comp[i],size=10,color='blue')

x=np.array(prod)
y=np.array(comp)
par = np.polyfit(x, y, 1, full=True)
slope=par[0][0]
intercept=par[0][1]
y_predicted = [slope*i + intercept  for i in x]

f.line(x,y_predicted,color='red')

#labels
f.title = "Productivity vs. Hourly Compensation"
f.xaxis.axis_label = "Net Productivity Per Hour Worked"
f.yaxis.axis_label = "Average Hourly Compensation"

def get():
    global f
    return f