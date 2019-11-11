import numpy as np

class Memoria(object):
    
    def __init__(self,n_bit,tamanho):
        
        self.memoria = np.zeros((tamanho,n_bit))

    def getLinha(self, linhaDeEsturcao):
        return self.memoria[linhaDeEsturcao]

    def setValorMemoria(self, linhaMemoria, saida_ULA):
        self.memoria[linhaMemoria]=np.copy(saida_ULA)

    def mostraValores(self):
        print (self.memoria)