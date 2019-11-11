import portasLogicas as pl
import operacoesAritmeticas as opA
import numpy as np

numero_de_instrucoes = 4

class Ula(object):

    def __init__(self, n_bit):

        self.instrucao = []
        self.A= np.zeros(n_bit)
        self.B= np.zeros(n_bit)
        self.saida= []

    def NOT(self):
        for i in range(0,len(self.A)):
            self.saida.append(pl.NOT(self.A[i]))
    
    def AND(self):
        for i in range(0,len(self.A)):
            self.saida.append(pl.AND(self.A[i],self.B[i]))

    def OR(self):
        for i in range(0,len(self.A)):
            self.saida.append(pl.OR(self.A[i],self.B[i]))

    def NAND(self):
        for i in range(0,len(self.A)):
            self.saida.append( pl.NAND(self.A[i],self.B[i]))
    
    def NOR(self):
        for i in range(0,len(self.A)):
            self.saida.append(pl.NOR(self.A[i],self.B[i]))

    def XOR(self):
        for i in range(0,len(self.A)):
            self.saida.append(pl.XOR(self.A[i],self.B[i]))
    def XNOR(self):
        for i in range(0,len(self.A)):
            self.saida.append(pl.XNOR(self.A[i],self.B[i]))

    def SUM(self):

        Cin=0
        
        for i in reversed(range(len(self.A))):
            saidas_sum=opA.SUM(self.A[i],self.B[i],Cin)
            resultado_SUM = saidas_sum[0]
            Cin = saidas_sum[1]
            self.saida.insert(0,resultado_SUM)

        if Cin == 1:
            print("overFlow")

    def SUB(self):

        Cin=0
        for i in reversed(range(len(self.A))):
            saidas_sum=opA.SUB(self.A[i],self.B[i],Cin)
            resultado_SUM = saidas_sum[0]
            Cin = saidas_sum[1]
            self.saida.insert(0,resultado_SUM)

        if Cin == 1:
            print("overFlow")

    def selecao(self):
        self.saida.clear()
        if self.instrucao == [0,0,0,1]:
            self.NOT()
        if self.instrucao == [0,0,1,0]:
            self.AND() 
        if self.instrucao == [0,0,1,1]:
            self.OR()
        if self.instrucao == [0,1,0,0]:
            self.NAND()
        if self.instrucao == [0,1,0,1]:
            self.NOR()
        if self.instrucao == [0,1,1,0]:
            self.XOR()
        if self.instrucao == [0,1,1,1]:
            self.XNOR()
        if self.instrucao == [1,0,0,0]:
            self.SUM()
        if self.instrucao == [1,0,0,1]:
            self.SUB()
        
    def setInstrucao(self,instrucao):

        self.instrucao = instrucao
    
    def getA(self):

        return self.A

    def getB(self):

        return self.B

    def setA(self, A):
        
            self.A=A 

    def setB(self, B):
            self.B=B

    def getSaida(self):
        return self.saida

    