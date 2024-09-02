class Passaro:
    def voar(self):
        print("Voando...")
    
    def emitirsom(self):
        pass

class Pato(Passaro):
    def __init__(self):
        print("Pato")
    
    
    def voar(self):
        print("Voando...")
    
    
    def emitirsom(self):
        print("Pato emitindo som...")
        print("Quack Quack")
    
    
    
class Pardal(Passaro):
    def __init__(self):
        print("Pardal")
    
    
    def voar(self):
        print("Voando...")
    
    
    def emitirsom(self):
        print("Pardal emitindo som...")
        print("Piu Piu")
        

pato = Pato()
pato.voar()
pato.emitirsom()
pardal = Pardal()
pardal.voar()
pardal.emitirsom()
