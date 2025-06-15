import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("https://raw.githubusercontent.com/subhajitdey295/Python_Employee_Career_Survey/refs/heads/main/Career%20Survey.csv")
# print(data)
print(data.head())
# print(data.columns)

# country = data['Your Current Country.'].value_counts()
# print(country)
# label = country.index
# counts = country.values
# colors = ['red','lightgreen']
# fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
# fig.update_layout(title_text = "Current Country ")
# fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30, marker = dict(colors = colors , line = dict(color = 'black', width = 3)))
# fig.show()


# question1 = data['Which of the below factors influence the most about your career aspirations ?']
# label = question1.index
# counts = question1.values
# colors =  ['black','yellow']
# fig = go.Figure(data = [go.Pie(labels = label , values = counts)])
# fig.update_layout(title_text = "Factors influencing career aspirations ")
# fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30, marker = dict(colors = colors , line =  dict(color = 'black', width = 3)))
# fig.show()

# question2 = data['Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.'].value_counts()
# print(question2)
# label = question2.index
# counts = question2.values
# colors = ['green','blue']
# fig = go.Figure(data = (go.Pie(labels = label , values = counts)))
# fig.update_layout(title_text = 'How many students to go for the Highrer Education for outside the country ')
# fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30, marker = dict(colors = colors , line =  dict(color = 'black', width = 3)))
# fig.show()

# question3 = data[  'How likely is that you will work for one employer for 3 years or more ?'].value_counts()
# print(question3)
# label = question3.index
# counts = question3.values
# colors = ['red','grey']
# fig = go.Figure(data = (go.Pie(labels = label , values = counts)))
# fig.update_layout(title_text = 'How many people to work ina a company for proper 3 years')
# fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 20, marker = dict(colors = colors, line = dict(color = 'black', width = 4)))
# fig.show()


question5 = data[ 'What is the most preferred working environment for you.'].value_counts()
print(question5)
label = question5.index
counts = question5.values
colors = ['red','lightgreen']
fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = "Preferred working environment ")
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 20 , marker = dict(colors = colors ,  line = dict(color = 'black', width =  4)))
fig.show()