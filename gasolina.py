import pandas as pd
import seaborn as sns

data = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data= data , x='venda', y='dia')
  grafico.set(title='Preço da gosolina por dia')
  