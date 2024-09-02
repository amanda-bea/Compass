class Aviao:
    
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "Azul"
        
    
    def __str__(self):
        return (f"O avião de modelo '{self.modelo}' possui uma velocidade máxima de "
                f"{self.velocidade_maxima} km/h, capacidade para {self.capacidade} passageiros "
                f"e é da cor {self.cor}.")
                
aviao1 = Aviao("BOIENG456", 1500, 400)
aviao2 = Aviao("Embraer Praetor 600", 863, 14)
aviao3 = Aviao("Antonov An-2", 258, 12)
print(aviao1)
print(aviao2)
print(aviao3)
        