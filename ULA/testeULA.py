from ula import Ula


ula=Ula(4)
A = [1,0,0,0,1,0,0,1]
B = [1,0,0,0,1,0,0,1]
C = [1,1,1,1,1,1,1,1]
ula.setA(A)
ula.setB(B)
ula.setInstrucao([0,0,0,1])

ula.selecao()
print(ula.getSaida())

ula.setInstrucao([0,0,1,0])
ula.selecao()
print(ula.getSaida())


ula.setInstrucao([0,0,1,1])
ula.selecao()
print(ula.getSaida())


ula.setInstrucao([0,1,0,0])
ula.selecao()
print(ula.getSaida())


ula.setInstrucao([0,1,0,1])
ula.selecao()
print(ula.getSaida())


ula.setInstrucao([0,1,1,0])
ula.selecao()
print(ula.getSaida())


ula.setInstrucao([0,1,1,1])
ula.selecao()
print(ula.getSaida())

ula.setInstrucao([1,0,0,0])
ula.selecao()
print(ula.getSaida())


ula.setInstrucao([1,0,0,1])
ula.selecao()
print(ula.getSaida())