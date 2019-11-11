from memoria_ram import Memoria 

def carregaMem(arquivo):
    
    listaDeBinarios = Memoria()
    binarios= []
    variaveis =[]

    listaDeVariaveis = open(arquivo+".txt",'r')    
    
    for i in listaDeVariaveis:
        variaves = i
        for j in variaves:
            if j == '0' or j =='1':
                binarios.append(int(j))

        listaDeBinarios.setMemoria(binarios)

        variaveis.clear()
        binarios.clear()            


    listaDeBinarios.mostraValores()
    listaDeVariaveis.close()

    return listaDeBinarios




