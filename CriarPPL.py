from  pulp import LpProblem,LpVariable,lpSum

matriz = [
    [0, 12, 11, 7, 10, 10, 9, 8, 6], 
    [12, 0, 8, 5, 9, 12, 14, 16, 17], 
    [11, 8, 0, 9, 15, 17, 8, 18, 14], 
    [7, 5, 9, 0, 7, 9, 11, 12, 12], 
    [10, 9, 15, 7, 0, 3, 17, 7, 15], 
    [10, 12, 17, 9, 3, 0, 18, 6, 15], 
    [9, 14, 8, 11, 17, 18, 0, 16, 8], 
    [8, 16, 18, 12, 7, 6, 16, 0, 11], 
    [6, 17, 14, 12, 15, 15, 8, 11, 0]
]

demandas = [0,10,15,18,17,3,5,9,4]

n_carros = 2
capacidade = 48


#Criei o modelo
modelo = LpProblem('PRV')

#Criei as variáveis de decisão
variaveis_decisao = {}
for k in range(n_carros):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            
            if i != j:
                variaveis_decisao[(i,j,k)] = LpVariable(name=f'X{i}{j}{k}')
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

#1° restrição

for k in range(n_carros):
    listaX = []
    listaY = []
    
    for i in range(1,len(matriz)):
        listaX.append(variaveis_decisao[(i,0,k)])
        
    for j in range(1,len(matriz)):
        listaY.append(variaveis_decisao[(0,j,k)])
        
    modelo += lpSum(listaX) - lpSum(listaY) == 0 
    
    listaX.clear()
    listaY.clear()
    
#2° restrição

for j in range(len(matriz)):
    
    for i in range(len(matriz)):
        for k in range(n_carros):
            if i != j:
                listaX.append(variaveis_decisao[(i,j,k)])
            else:
                None

    modelo += lpSum(listaX) == 1
    listaX.clear()

print(modelo)









