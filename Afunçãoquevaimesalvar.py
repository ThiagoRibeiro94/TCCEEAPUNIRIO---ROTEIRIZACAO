
matriz = [[0,0,0,0],
          [1,1,1,1],
          [2,2,2,2],
          [3,3,3,3]]

lista1 = [0,1,2,3]
lista2 = [0,1,2,3]
lista3 = [0,1,2,3]

listaexcluir = [1,2,3]

def ExcluirDadosMatriz(matriz,lista1,lista2,lista3,listaexcluir):
    
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
            
    print(matrizIntermediaria)
    
    for linha in matrizIntermediaria:
        novaLinha = []
        for i in range(len(linha)):
            index = i
            if index in listaexcluir:
                None
            else:
                novaLinha.append(i)         
        novaMatriz.append(novaLinha)
        
        
    for i in range(len(lista1)):
        
        if i in  listaexcluir:
            None
        else:
            novaLista1.append(lista1[i])
            novaLista2.append(lista2[i])
            novaLista3.append(lista3[i])
    
    
    return novaMatriz, novaLista1,novaLista2,novaLista3
                
            
    
    
        
        
        
        
print(ExcluirDadosMatriz(matriz,lista1,lista2,lista3,listaexcluir))


