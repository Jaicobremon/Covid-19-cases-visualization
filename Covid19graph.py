#Code by Jaicob Remon

#Importing all modules
import csv
import pandas as pd
import plotly.express as px

#Telling program which database to read
df = pd.read_csv("Copyofdata.csv")

#Creating scatterplot
fig = px.scatter(df, x = "Date", y = "Cases", color = "Country", title = "Covid 19 cases over time")

#Showing scatterplot on screen
fig.show()

#Telling program which database to read
df2 = pd.read_csv("Copyofdata.csv")

#Creating line graph
fig = px.line(df2, x = "Date", y = "Cases", color = "Country", title = "Covid 19 cases over time")

#Showing linegraph on screen
fig.show()



