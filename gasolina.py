import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("gasolina.csv")

grafico = sns.lineplot(x='dia' , y='venda',data=data, marker='*', markerfacecolor='limegreen', markersize=15)

grafico.set(title='preço da gasolina em 10 dias', xlabel='preço')