from bokeh.plotting import figure
import numpy as np

import annual_working_hours_per_worker
import world_happiness

d_annual_working_hours_per_worker = annual_working_hours_per_worker.get()
d_world_happiness = world_happiness.get()

graph1x,graph1y = [],[]
for i in d_annual_working_hours_per_worker:
    for c in d_world_happiness:
        if i==c:
            graph1x.append(d_annual_working_hours_per_worker[i])
            graph1y.append(d_world_happiness[c])

f = figure()
for i in range(len(graph1x)):
    f.circle(graph1x[i],graph1y[i],size=10,color="blue")

x=np.array(graph1x)
y=np.array(graph1y)
par = np.polyfit(x, y, 1, full=True)
slope=par[0][0]
intercept=par[0][1]
y_predicted = [slope*i + intercept  for i in x]

f.line(x,y_predicted,color='red')

#RETURNS FIGURE. JUST DO show(f)
def get():
    global f
    return f