import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
#print(df.groupby('level')['attempt].mean())

studentdf = df.loc[df['studentId']=='TRL_xsl']
print(studentdf.grpupby('level')['attempt'].mean())

fig = go.Figure(go.bar(
    x = df.groupby('level')['attempt'].mean(),
    y = ['Level 1', 'Level 2','Level 3','Level 4']
))
fig.show()

fig = go.Figure(go.Bar(
    x = studentdf.groupby('level')['attempt'].mean(),
    y = ['Level 1','Level 2','Level 3','Level 4']
))
fig.show()