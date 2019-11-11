from memoria_ram import Memoria
from ula import Ula
import carregaMemoria as cm
from clock import Clock

#Voce parou aqui e tem que fazer os teste ainda

class Uc(object):
    
    def __init__(self, n_bit,time):
        self.memoriaNumeros = cm.carregaMem("memoria")
        self.memoriaComandos = cm.carregaMem("comando")
        self.pc = 0
        self.ula = Ula(n_bit)
        self.clock = Clock(time)


    def setComando(self):
        self.ula.setInstrucao(self.memoriaComandos.getLinha(self.pc))
        self.pc=self.pc+1

    def setVariaveis_A(self):
        self.ula.setA(self.memoriaNumeros.getLinha(self.pc))

    def setVariaveis_B(self):
        self.ula.setB(self.memoriaNumeros.getLinha((self.pc)+1))

    def getComando(self):
        return self.memoriaComandos.getLinha(self.pc)

    def getVariavel_A(self):
        return self.memoriaNumeros.getLinha(self.pc)
    
    def getVariavel_B(self):
        return self.memoriaNumeros.getLinha((self.pc)+1)

    def run_clock(self):
        self.clock.perildo()

    def getClockStatus(self):
        return self.clock.getEstadoClock()

    def getExitUla(self):

        return self.ula.getSaida()

    def burn_all_nero(self):
        while len(self.pc) != len(self.memoriaComandos) :

            if self.getClockStatus != 0:
                
                self.setVariaveis_A()
                self.setVariaveis_B()
                self.setComando()
                self.memoriaNumeros.setValorMemoria(self.pc, self.getExitUla())
                self.run_clock()

            self.run_clock() 
                
