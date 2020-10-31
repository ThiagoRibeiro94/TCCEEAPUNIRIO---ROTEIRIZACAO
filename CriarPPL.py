from  pulp import *
from itertools import combinations,permutations
import pandas as pd
import json
from random import randint

def CarregarJson(nomeArquivo):
    with open(nomeArquivo, 'r') as f:
        return json.load(f)


def ExcluirDadosMatriz(matriz=[],lista1=[],lista2=[],lista3=[],listaexcluir=[]):
    
    novaMatriz =[]
    novaLista1 =[]
    novaLista2 =[]
    novaLista3 =[]
    matrizIntermediaria = []
    
    for linha in matriz: 
        index = matriz.index(linha)
        if index in listaexcluir:
            None
        else:
            matrizIntermediaria.append(linha)
                
    for linha in matrizIntermediaria:
        novaLinha = []
        for i in range(len(linha)):
            index = i
            if index in listaexcluir:
                None
            else:
                novaLinha.append(linha[i])         
        novaMatriz.append(novaLinha)
        
    if lista1!=[] and lista2!=[] and lista3!=[]:
        for i in range(len(lista1)):
            if i in listaexcluir:
                None
            else:
                novaLista1.append(lista1[i])
                novaLista2.append(lista2[i])
                novaLista3.append(lista3[i])
    
    
    return novaMatriz, novaLista1,novaLista2,novaLista3
                
        
        
        

listaexcluir = [1,4,6,9,14,16,19,22,23,26,2,8,17,18,25]
total_pessoas = CarregarJson('2020JSON/jsonPessoas.json')["pessoas"]
matriz = CarregarJson('2020JSON/jsonMinutos.json')["distanciaEmMinutos"]
nos = CarregarJson('2020JSON/jsonEndereco.json')["endereco"]
gastos = CarregarJson('2020JSON/jsonGasto.json')['Gasto']



dadosDepoisExclusão = ExcluirDadosMatriz(matriz, total_pessoas, gastos, nos, listaexcluir)
matriz = dadosDepoisExclusão[0]
total_pessoas= dadosDepoisExclusão[1]
gastos = dadosDepoisExclusão[2]
nos = dadosDepoisExclusão[3]

demandas = total_pessoas

n_carros = 2
capacidade = 480
vertices = len(matriz)

#Criei o modelo
modelo = LpProblem('PRV')

#Criei as variáveis de decisão
variaveis_decisao = {}
listaVD = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','X','Z']
for k in range(n_carros):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            
            if i != j:
                variaveis_decisao[(i,j,k)] = LpVariable(name=f'{listaVD[randint(0,18)]}{i}{j}{k}',cat='Binary')
            else:
                None
        
#Criar função objetivo
listaFo = []
for k in range(n_carros):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            
            if i != j:
                listaFo.append(matriz[i][j]*variaveis_decisao[(i,j,k)])

modelo += lpSum(listaFo)
listaFo.clear()

# 1° restrição
lista_aux_1 =[]
lista_aux_2 = []
for k in range(n_carros):
    i =0 
    for j in range(vertices):
        if i != j:
            lista_aux_1.append(variaveis_decisao[(i,j,k)])
    modelo += lpSum(lista_aux_1) == 1
    lista_aux_1.clear()


# 2° restrição
for k in range(n_carros):
    j =0 
    for i in range(vertices):
        if i != j:
            lista_aux_1.append(variaveis_decisao[(i,j,k)])
    modelo += lpSum(lista_aux_1) == 1
    lista_aux_1 = []

# 3° restrição

for k in range(n_carros):
    for h in range(1,vertices):
        for b in range(vertices):
            if h!=b:
                lista_aux_1.append(variaveis_decisao[(h,b,k)] - variaveis_decisao[(b,h,k)])
                #print(lista_aux_1)
                #print('')
                #print(lpSum(lista_aux_1))
                #print('========================================================================================================')
        modelo += lpSum(lista_aux_1) == 0
        lista_aux_1 = []
        lista_aux_2 = []


# 4° restrição

for i in range(1,vertices):
    for j in range(vertices):
        for k in range(n_carros):
            if i != j:
                lista_aux_1.append(variaveis_decisao[(i,j,k)])
    
    modelo += lpSum(lista_aux_1) == 1
    lista_aux_1.clear()


# 5° restrição - A mais dificil

lista_vertices = [i for i in range(1,vertices)]
lista_vertices_com_origem = [i for i in range(vertices)]


for S in lista_vertices[1:]:
    for k in range(n_carros):
        combinações = combinations(lista_vertices_com_origem,S)

        for combinação in combinações:
            pares = combinations(combinação,2)
            for par in pares:
                i = par[0]
                j = par[1]
                lista_aux_1.append(variaveis_decisao[(i,j,k)])
                lista_aux_1.append(variaveis_decisao[(j,i,k)])
                
            modelo += lpSum(lista_aux_1) <= S-1
            lista_aux_1.clear()
            lista_aux_2.clear()


#6° restrição

for k in range(n_carros):
    for i in range(vertices):
        for j in range(vertices):
            if i!=j:
                lista_aux_1.append(matriz[i][j]*variaveis_decisao[(i,j,k)])
                
    modelo += lpSum(lista_aux_1) <= capacidade
    lista_aux_1.clear()


print('modelo criado')
status = modelo.solve()

print(LpStatus[status])

for chave,valor in variaveis_decisao.items():
    
    if value(valor) != 0:
        print(f'{chave} == {value(valor)}')


'''
listaRest = list(modelo.constraints.values())

for i in listaRest[25:45]:
    print(i)
    print('=============================================================================================')
'''








