import pandas as pd
import plotly.express as px
DF = pd.read_csv('data.csv')
figure = px.scatter(DF, x = "Population", y = "Per capita", title = "P" , size = "Percentage", color = "Country", size_max = 50)
figure.show()
