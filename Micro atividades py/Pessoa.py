class Pessoa:
    def __init__(self, nome, numero_conta, data_abertura_conta, status):
        self.__nome = nome
        self.__numero_conta = numero_conta
        self.__data_abertura_conta = data_abertura_conta
        self.__status = status

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def numero_conta(self):
        return self.__numero_conta

    @numero_conta.setter
    def numero_conta(self, valor):
        self.__numero_conta = valor

    @property
    def data_abertura_conta(self):
        return self.__data_abertura_conta

    @data_abertura_conta.setter
    def data_abertura_conta(self, valor):
        self.__data_abertura_conta = valor

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor

    def imprimir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"Número da Conta: {self.__numero_conta}")
        print(f"Data de Abertura da Conta: {self.__data_abertura_conta}")
        print(f"Status: {self.__status}")
