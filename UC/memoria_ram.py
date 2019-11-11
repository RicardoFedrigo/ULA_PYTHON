class Memoria(object):
    
    def __init__(self):
        
        self.memoria = []

    def getLinha(self, linhaDeEsturcao):
        return self.memoria[linhaDeEsturcao]

    def setValorMemoria(self, linhaMemoria, saida_ULA):
        self.memoria.insert(linhaMemoria,saida_ULA)

    def setMemoria(self,n_bit):
        self.memoria.append(n_bit)

    def mostraValores(self):
        print (self.memoria)