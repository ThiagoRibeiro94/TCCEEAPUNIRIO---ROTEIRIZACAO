from itertools import permutations
import pandas as pd
import json


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
capacidade = 58
arestas = {}
for i in range(1,len(matriz)):
    for j in range(1,len(matriz)):
        
            if matriz[i][j] != 0:
                saving = matriz[i][0] + matriz[0][j] - matriz[i][j]
                arestas[(i,j)] = saving
            else:
                None
            

arestas_ordenada = {}
for item in sorted(arestas, key = arestas.get, reverse = True):
    arestas_ordenada[item]=arestas[item]

sb = []    
for i in range(1,len(matriz)):
      sb.append([i])

#print(arestas_ordenada)
#print(sb)

for aresta in arestas_ordenada:
    print("============================")
    print(f'Par do estudo:{aresta}')
    
    for rota in sb:
        
        if aresta[0] in rota:
            sbOrigem = sb.index(rota)
        
        if aresta[1] in rota:
            sbDestino = sb.index(rota)
            
    if sbOrigem != sbDestino:
        
        rota1 = sb[sbOrigem]
        rota2 = sb[sbDestino]
        
        finalRotaOrigem = sb[sbOrigem][-1]
        comecoRotaOrigem = sb[sbOrigem][0]
        comecoRotaDestino = sb[sbDestino][0]
        finalRotaDestino = sb[sbDestino][-1]
        
        if (finalRotaOrigem == aresta[0] and comecoRotaDestino == aresta[1]) or (aresta[1] == comecoRotaDestino):
            print('As rotas podem ser juntadas, tem que testar a capacidade:')
            
            soma_demanda = 0
            
            for i in rota1:
                soma_demanda += demandas[i]
            
            for j in rota2:
                soma_demanda += demandas[j]
            
            
            if soma_demanda <= capacidade:
                print(f'A soma das demandas da {soma_demanda}, o que é menor que 40')
                
                sb.remove(rota1)
                sb.remove(rota2)
                
                nova_rota = rota1 + rota2
                sb.append(nova_rota)
                
                print(f'O novo conjunto de sb pode ser visto abaixo:')
                print(f'sb = {sb}')
                
                
            else:
                print(f'As rotas não podem ser juntadas pois a soma das demandas é maior que 40')
        
        else:
            print(f'Não pode porque {aresta[1]} é um nó interno.')
            

    else:
        print(f'A aresta {aresta} estão na mesma rota, portanto nada feito')
            

for rota in sb:
    print('========================================')
    gasto = 0 
    pessoas = 0
    tempo = 0
    for i in rota:
        gasto += gastos[i]
        pessoas += total_pessoas[i]
        print(nos[i])
        
        index_elemento_rota = rota.index(i)
        
        try:
            tempo += matriz[rota[index_elemento_rota]][rota[index_elemento_rota+1]]
        except:
            None
            
    print(tempo)
    print(gasto)
    print(pessoas)           