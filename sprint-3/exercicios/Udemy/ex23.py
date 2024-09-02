class Calculo:
    def soma(self,x,y):
        print(f"Somando: {x}+{y} = {x + y}")

        
        
    def sub(self,x,y):
        print(f"Subtraindo: {x}-{y} = {x - y}")
        

x = 4
y = 5

calculo = Calculo()

resultado_soma = calculo.soma(x, y)
resultado_subtracao = calculo.sub(x, y)
        