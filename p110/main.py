import plotly.figure_factory as ff
import statistics
import random 
import csv
import pandas as pd

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)

print("population mean: ",population_mean)
print("standerd deviation: ",std_deviation)

fig=ff.create_distplot([data],["reading_time"],show_hist=False)
fig.show()

#code to find mean std dev of 100 data points
dataset=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)
mean=statistics.mean(dataset)
std_deviation=statistics.stdev(dataset)

print("sample mean: ",mean)
print("standerd deviation of sample: ",std_deviation)