class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

p1 = pessoa("Júlia", 15)
p2 = pessoa("Nuno", 10)
p1.exibir_informacoes()
p2.exibir_informacoes()