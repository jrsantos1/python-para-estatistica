import pandas as pd 
from IPython.display import display 
import seaborn as sns

dados = pd.read_csv('dados.csv')

dados = pd.DataFrame({'Profissão': [1, 2, 3, 1, 2, 2, 2, 3, 3, 2, 1, 3]})

frequencia = dados['Profissão'].value_counts()
percentual = dados['Profissão'].value_counts(normalize = True)

print(frequencia)
print(percentual)


dist_frequencia_qualitativa = pd.DataFrame({'Frequencia': frequencia, 'Porcentagem': percentual})
dist_frequencia_qualitativa.rename(index = {1: 'Estatistico', 2: 'Cientista de Dados', 3: 'Programador Python'}, inplace=True)
dist_frequencia_qualitativa.rename_axis('Profissão', axis='columns', inplace=True)

print(dist_frequencia_qualitativa)