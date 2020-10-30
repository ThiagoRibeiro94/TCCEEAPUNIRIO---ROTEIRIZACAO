matrizOld = [
[0,12,11,7,10,10,9,8,6,12],
[0,0,8,5,9,12,14,16,17,22],
[0,0,0,9,15,17,8,18,14,22],
[0,0,0,0,7,9,11,12,12,17],
[0,0,0,0,0,3,17,7,15,18],
[0,0,0,0,0,0,18,6,15,15],
[0,0,0,0,0,0,0,16,8,16],
[0,0,0,0,0,0,0,0,11,11],
[0,0,0,0,0,0,0,0,0,10],
[0,0,0,0,0,0,0,0,0,0]
]




matriz = []
for i in range(len(matrizOld)):
    linha = []
    for j in range(len(matrizOld)):
        
        if i == j :
            linha.append(0)
        
        elif matrizOld[i][j] == 0:
            linha.append(matrizOld[j][i])
            
        else:
            linha.append(matrizOld[i][j])
            
    matriz.append(linha)

demandas = [0,10,15,18,17,3,5,9,4,6]
capacidade = 40
arestas = {}
for i in range(1,len(matriz)):
    for j in range(1,len(matriz)):
        
        if (j,i) not in arestas.keys():
        
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
            
            
            
            

            
        
      
      
      
      
      
      