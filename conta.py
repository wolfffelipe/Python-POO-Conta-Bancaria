class Conta(): #classe Conta
    def __init__(self, numero, titular, saldo, limite = 1000.0): #aqui seria o nosso construtor
        self.__numero = numero #__ para atributos privados 
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {}: {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): #__ cria o método privado
        saque_limite = self.__saldo + self.__limite
        return valor_a_sacar <= saque_limite #retorna TRUE ou FALSE

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"Saldo insuficiente para o valor de {valor}") #f permite usar a variável entre {}

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #property: é a mesma coisa de criar um método get_saldo, porém, utilizando o property, 
    #na hora de chamar o método, não usamos mais os parênteses
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @property
    def titular(self):
        return self.__titular

    #dessa forma ao invés de usar "conta.set_limite(100)"", usamos "conta.limite = 100"
    @limite.setter 
    def limite(self, novo_limite):
        self.__limite = novo_limite

    #staticmethod cria métodos estáticos que podem ser chamados como Conta.codigo_banco
    @staticmethod
    def codigo_banco():
        return "001"