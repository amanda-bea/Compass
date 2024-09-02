class Lampada:
    def __init__(self, ligada=False):
        self.ligada = ligada
        
    def liga(self):
        self.ligada = True
        
    def desliga(self):
        self.ligada = False
    
    def esta_ligada(self):
        return self.ligada
        
lampada = Lampada(False)
lampada.liga()
print("A lâmpada está ligada?", lampada.esta_ligada())
lampada.desliga()
print("A lâmpada ainda está ligada?", lampada.esta_ligada())
    
        