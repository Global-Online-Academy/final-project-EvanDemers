import graph1, graph2, working_hours_vs_gdp,graph4

f1,f2,f3,f4 = graph1.get(),graph2.get(),working_hours_vs_gdp.get(),graph4.get()

from bokeh.layouts import gridplot
from bokeh.plotting import show

show(gridplot([[f1,f3],[f2,f4]]))