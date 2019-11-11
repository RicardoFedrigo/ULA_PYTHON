
class Memoria:
    
    def __init__(self, n_bit,tamanho):
        
        try:
            validar(self,n_bit,tamanho)
        except ValueError :
            return 0

        self.n_bit = int(n_bit)
        self.tamanho = int(tamanho)


    def validar(self, n_bit, tamanho):
        
        if type(n_bit) != type(int):
            print("O n_bit nao 'e um inteiro")
            return ValueError
        
        if tamanho != type(int):
            print("O tamanho nao 'e um inteiro")
            return ValueError

        if tamanho%2 != 0:
            print("O tamanho tem que ser multiplo de 2")
            return
        
        if n_bit < 3:
            print ("Tamanho de bit's menor que requerido")
            return ValueError
\