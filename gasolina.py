import pandas as pd
import seaborn as sns

data = pd.read_csv('gasolina.csv')

grafico = sns.barplot(data=data,x='dia',y='venda', palette='pastel')