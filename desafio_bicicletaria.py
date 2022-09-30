class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1


    def buzinar(self):
        print("Som de buzina")


    def parar(self):
        print("bicicleta parada")


    def correr(self):
        print("veloz e furioso")


    def troca_marcha(self, n_marcha):
        print("trocando marcha")

        def _troca_marcha():
            if n_marcha > self.marcha:
                print("marcha trocada")
            else:
                print("marcha não trocada")



    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

b1 = bicicleta('vermelha', 'caloi', 2022, 599)

#b1.buzinar()
#b1.correr()
#b1.parar()

