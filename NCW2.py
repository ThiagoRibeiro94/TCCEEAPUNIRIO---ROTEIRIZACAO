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
                
        
        
        

listaexcluir = [1,2,4,6,8,9,14,16,17,18,19,22,25,26]
total_pessoas = CarregarJson('2020JSON/jsonPessoas.json')["pessoas"]
minutos = CarregarJson('2020JSON/jsonMinutos.json')["distanciaEmMinutos"]
nos = CarregarJson('2020JSON/jsonEndereco.json')["endereco"]
gastos = CarregarJson('2020JSON/jsonGasto.json')['Gasto']



dadosDepoisExclusão = ExcluirDadosMatriz(minutos, total_pessoas, gastos, nos, listaexcluir)
minutos = dadosDepoisExclusão[0]
total_pessoas= dadosDepoisExclusão[1]
gastos = dadosDepoisExclusão[2]
nos = dadosDepoisExclusão[3]


indices = []
for i in range(len(nos)):
    indices.append(i)

indices = indices[1:-1]


#Ver a econômia gerada pelos pares.
dicionario_economias = {}
for pares in permutations(indices,2):
    economia = minutos[0][pares[0]] + minutos[0][pares[1]] - minutos[pares[0]][pares[1]]
    dicionario_economias[pares] = economia


#Ordenar o dicionário_economias do maior para o menor
dicionario_economias_ordenado = {}
for item in sorted(dicionario_economias, key = dicionario_economias.get,reverse=True):
    dicionario_economias_ordenado[item] = dicionario_economias[item]

print(dicionario_economias_ordenado)
#Começando o passo3,4 e 5
lista_pontos = list(dicionario_economias_ordenado.keys())


def InteracaoCW(dicionario,lista,tempo,pessoas,rota,lista_rotas,minutos,total_pessoas):
    if lista == []:
        controlador = 1
        return (dicionario,lista,tempo,pessoas,rota,lista_rotas,controlador)
    else:
        controlador = 0 
        for chave in dicionario.keys():
            minutos_entre_pontos = minutos[chave[0]][chave[1]]
            pessoas_entre_pontos = total_pessoas[chave[0]] + total_pessoas[chave[1]]
            
            if rota[-1] == chave[0] and chave in lista:
                if tempo + minutos_entre_pontos <= 480 and pessoas + pessoas_entre_pontos <= 60:

                    rota.append(chave[1])
                    tempo += minutos_entre_pontos
                    pessoas += pessoas_entre_pontos

                    listaCopy = lista.copy()
                    for i in lista:
                        if i[0] == chave[0] or i[1]==chave[0]:
                            listaCopy.remove(i)
                        
                    lista = listaCopy
                    
                    return (dicionario,lista,tempo,pessoas,rota,lista_rotas,controlador)

                else:
                    rota.append(0)
                    lista_rotas.append(rota)
                    rota = [0]
                    rota.append(chave[1])
                    tempo = minutos_entre_pontos
                    pessoas = pessoas_entre_pontos

                    listaCopy = lista.copy()
                    for i in lista:
                        if i[0] == chave[0] or i[1]==chave[0]:
                            listaCopy.remove(i)
                        
                    lista = listaCopy
                    
                    return (dicionario,lista,tempo,pessoas,rota,lista_rotas,controlador)

            elif rota[-1]==0 and chave in lista:
                rota.append(chave[0])
                rota.append(chave[1])
                tempo = minutos_entre_pontos
                pessoas = pessoas_entre_pontos

                listaCopy = lista.copy()
                for i in lista:
                    if i[0] == chave[0] or i[1]==chave[0]:
                        listaCopy.remove(i)
                        
                lista = listaCopy
                return (dicionario,lista,tempo,pessoas,rota,lista_rotas,controlador)

            else:
                continue

tempo = 0 
pessoas = 0 
rota = [0]
lista_rotas = []
lista = lista_pontos
controlador = 0

while controlador == 0:
    try:
        dicionario = resultado[0]

        lista = resultado[1]
        tempo = resultado[2]
        pessoas = resultado[3]
        rota = resultado[4]
        lista_rotas = resultado[5]
        controlador = resultado[6]
        resultado = InteracaoCW(dicionario,lista,tempo,pessoas,rota,lista_rotas,minutos,total_pessoas)
        
    except:

        dicionario = dicionario_economias_ordenado
        lista = lista_pontos
        tempo = 0
        pessoas = 0
        rota = [0]
        lista_rotas = []
        controlador = 0
        resultado = InteracaoCW(dicionario,lista,tempo,pessoas,rota,lista_rotas,minutos,total_pessoas)

rota.append(0)
lista_rotas.append(rota)

def CriarRotarCSV(lista_rotas):
    cont = 0
    for route in lista_rotas:
        lista_nome = []
        for i in route:
            lista_nome.append(nos[i])
        dados = pd.DataFrame(lista_nome, columns=['endereco'])
        dados.to_csv(f'2020Rotas/rota{cont}.csv', index=False)
        cont += 1

criarRotas = CriarRotarCSV(lista_rotas)

lista_tempo = []
lista_metros = []
lista_pessoas = []
lista_gasto = []

for route in lista_rotas:
    tempo = 0
    distancia = 0
    pessoas = 0
    gasto = 0
    for ponto in range(len(route)):
        try:
            tempo = tempo + minutos[route[ponto]][route[ponto+1]]
            pessoas = pessoas + total_pessoas[route[ponto]]
            gasto = gasto + gastos[route[ponto]]
        except:
            None

    lista_tempo.append(tempo)
    lista_pessoas.append(pessoas)
    lista_gasto.append(gasto)



print(lista_tempo)
print(lista_pessoas)
print(lista_gasto)
for i in range(len(lista_rotas)):
    print("=======================================================================")
    print(f'Rota {i}')
    print(f'Rota:{lista_rotas[i]}')
    print(" ")
    print(" ")
    print(f'Legenda:')
    print(" ")
    for j in lista_rotas[i]:
        print(f'- {nos[j]}')

    print(" ")
    print(" ")

    print(" ")
    print(f'Tempo gasto na rota: {lista_tempo[i]} minutos')
