class carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

carro1 = carro("Fiat", "Palio", 1997)
carro2 = carro("desconhecida", "feio", 2024)
carro1.exibir_detalhes()
carro2.exibir_detalhes()
