import seaborn as sns
import pandas as pd

data = pd.read_csv("gasolina.csv")

sns.lineplot(x='dia' , y='venda',data=data)