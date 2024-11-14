class animal:
    def emitir_som():
        pass
class cachorro(animal):
    def emitir_som(self):
        print("Au au!")
class gato(animal):
    def emitir_som(self):
        print("Miau!")

cachorro = cachorro()
gato = gato()
cachorro.emitir_som()
gato.emitir_som()