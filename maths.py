import plotly.figure_factory as ff
import csv
import statistics
import plotly.graph_objects as go
import pandas as pd
import random
import plotly_express as px
df= pd.read_csv("datain.csv")
maths=df["math score"].tolist()
mean=statistics.mean(maths)
mode=statistics.mode(maths)
median=statistics.median(maths)
stdev=statistics.stdev(maths)
fst_start,fst_end=mean-stdev,mean+stdev
sst_start,sst_end=mean-(2*stdev),mean+(2*stdev)
tst_start,tst_end=mean-(3*stdev),mean+(3*stdev)
fig =ff.create_distplot([maths],["maths"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[fst_start,fst_start],y=[0,0.17],mode="lines",name="st1_start`"))
fig.add_trace(go.Scatter(x=[fst_end,fst_end],y=[0,0.17],mode="lines",name="st1_end"))
fig.add_trace(go.Scatter(x=[sst_start,sst_start],y=[0,0.17],mode="lines",name="st2_start`"))
fig.add_trace(go.Scatter(x=[sst_end,sst_end],y=[0,0.17],mode="lines",name="st2_end"))
fig.show()
list_data_1=[maths for maths in maths if maths >fst_start and maths <fst_end]
list_data_2=[maths for maths in maths if maths >sst_start and maths <sst_end]
list_data_3=[maths for maths in maths if maths >tst_start and maths <tst_end]
print(format(len(list_data_1)*100/len(maths)))
print(format(len(list_data_2)*100/len(maths)))
print(format(len(list_data_3)*100/len(maths)))



fig=ff.create_distplot([maths],["maths"],show_hist=False)
fig.show()