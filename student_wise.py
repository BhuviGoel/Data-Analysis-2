import pandas as pd
import csv
import plotly.express as px

data = pd.read_csv(r"C:\Users\bhuvi\Google Drive\Code\Python\Project 107 - Data Analysis\data.csv")
mean_std = data.groupby(["student_id","level"],as_index = False)["attempt"].mean()
fig = px.scatter(mean_std, x ="student_id", y = "level", size = "attempt", color = "attempt" )
fig.show()