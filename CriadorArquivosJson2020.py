import pandas as pd
import json

dados = pd.read_csv('distanciasFD.csv')

#Criar jsonEndereco.json

vertices = list(dados['municipios'])

with open('2020JSON/jsonEndereco.json','w') as arquivo:
    jsonEndereco = {"endereco":vertices}
    json.dump(jsonEndereco,arquivo)
    
#Criar jsonMinutos.json
matrizMinutos = []

for i in range(dados.shape[1]-1):
    linha = list(dados.iloc[i,1:])   
    matrizMinutos.append(linha)

for i in range(len(matrizMinutos)):#Foi necessário pois int64 não são transformados em json
    for j in range(len(matrizMinutos)):
        matrizMinutos[i][j] = float(matrizMinutos[i][j])

with open('2020JSON/jsonMinutos.json','w') as arquivo:
    jsonMinutos = {"distanciaEmMinutos":matrizMinutos}
    json.dump(jsonMinutos,arquivo)

#Criar jsonPessoas.json

dados2 = pd.read_csv('PessoasEPassagens.csv')
n_passageiros = list(dados2['Quantidade'])
gasto_passagem = list(dados2['total'])


with open('2020JSON/jsonPessoas.json','w') as arquivo:
    jsonPessoas = {"pessoas":n_passageiros}
    json.dump(jsonPessoas,arquivo)
    
with open('2020JSON/jsonGasto.json','w') as arquivo:
    jsonGasto = {"Gasto":gasto_passagem}
    json.dump(jsonGasto,arquivo)


