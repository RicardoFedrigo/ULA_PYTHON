import portasLogicas as pl 
import operacoesAritmeticas as opa
print("--------Saidas portas Logicas:-----------")

print("")
print("_____________Porta NOT_____________")
print("Saida A=0: ",pl.NOT(0))
print("Saida A=0: ",pl.NOT(1))

print("")
print("_____________Porta AND_____________")
print("Saida A=0 , B=0 : ",pl.AND(0,0))
print("Saida A=0 , B=1 : ",pl.AND(0,1))
print("Saida A=1 , B=0 : ",pl.AND(1,0))
print("Saida A=1 , B=1 : ",pl.AND(1,1))

print("")
print("_____________Porta OR_____________")
print("Saida A=0 , B=0 : ",pl.OR(0,0))
print("Saida A=0 , B=1 : ",pl.OR(0,1))
print("Saida A=1 , B=0 : ",pl.OR(1,0))
print("Saida A=1 , B=1 : ",pl.OR(1,1))

print("")
print("_____________Porta NAND_____________")
print("Saida A=0 , B=0 : ",pl.NAND(0,0))
print("Saida A=0 , B=1 : ",pl.NAND(0,1))
print("Saida A=1 , B=0 : ",pl.NAND(1,0))
print("Saida A=1 , B=1 : ",pl.NAND(1,1))

print("")
print("_____________Porta NOR_____________")
print("Saida A=0 , B=0 : ",pl.NOR(0,0))
print("Saida A=0 , B=1 : ",pl.NOR(0,1))
print("Saida A=1 , B=0 : ",pl.NOR(1,0))
print("Saida A=1 , B=1 : ",pl.NOR(1,1))

print("")
print("_____________Porta XOR_____________")
print("Saida A=0 , B=0 : ",pl.XOR(0,0))
print("Saida A=0 , B=1 : ",pl.XOR(0,1))
print("Saida A=1 , B=0 : ",pl.XOR(1,0))
print("Saida A=1 , B=1 : ",pl.XOR(1,1))

print("")
print("_____________Porta XNOR_____________")
print("Saida A=0 , B=0 : ",pl.XNOR(0,0))
print("Saida A=0 , B=1 : ",pl.XNOR(0,1))
print("Saida A=1 , B=0 : ",pl.XNOR(1,0))
print("Saida A=1 , B=1 : ",pl.XNOR(1,1))


print("--------Saidas operacoes aritmeticas:-----------")

print("____________SUM______________")

print("  Saidas SUM: (S,Cout)" )
print("1-Saidas SUM:", opa.SUM(0,0,0))
print("2-Saidas SUM:", opa.SUM(0,1,0))
print("3-Saidas SUM:", opa.SUM(1,0,0))
print("4-Saidas SUM:", opa.SUM(1,1,0))
print("5-Saidas SUM:", opa.SUM(0,0,1))
print("6-Saidas SUM:", opa.SUM(0,1,1))
print("7-Saidas SUM:", opa.SUM(1,0,1))
print("8-Saidas SUM:", opa.SUM(1,1,1))


print("____________SUB_______________")

print("  Saidas SUB: (S,Cout)" )
print("1-Saidas SUB:", opa.SUB(0,0,0))
print("2-Saidas SUB:", opa.SUB(0,1,0))
print("3-Saidas SUB:", opa.SUB(1,0,0))
print("4-Saidas SUB:", opa.SUB(1,1,0))
print("5-Saidas SUB:", opa.SUB(0,0,1))
print("6-Saidas SUB:", opa.SUB(0,1,1))
print("7-Saidas SUB:", opa.SUB(1,0,1))
print("8-Saidas SUB:", opa.SUB(1,1,1))
