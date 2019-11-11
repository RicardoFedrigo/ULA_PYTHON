from memoria import Memoria

m = Memoria(11,8)
m.setValorMemoria(3,[0,1,0,0,1,0,1,1,1,0,0])
m.mostraValores()
print(m.getLinha(3))