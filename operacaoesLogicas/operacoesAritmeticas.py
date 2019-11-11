import portasLogicas as pl 


#A saida de ser um tupla onde [S,Cout]
def SUM(A,B,Cin):

    return (pl.XOR(pl.XOR(A,B),Cin),(pl.OR(pl.AND(pl.XOR(A,B), Cin),pl.AND(A,B))))

def SUB(A,B,Cin):

    return (pl.XOR(pl.XOR(A,B),Cin),(pl.OR(pl.AND(not(pl.XOR(A,B)), Cin),pl.AND((not A),B))))


