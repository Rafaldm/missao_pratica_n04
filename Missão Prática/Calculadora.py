class Calculadora:
    def __init__(self, valorA=0, valorB=0, operacao='+'):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao

    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valor):
        self.__valorA = valor

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valor):
        self.__valorB = valor

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self, operacao):
        operacoes_validas = ['+', '-', '*', '/']
        return operacao in operacoes_validas

    def calcular(self):
        if not self.validarOperacao(self.__operacao):
            print(f"Operação inválida: {self.__operacao}")
            exit()

        if self.__operacao == '+':
            return self.__valorA + self.__valorB
        elif self.__operacao == '-':
            return self.__valorA - self.__valorB
        elif self.__operacao == '*':
            return self.__valorA * self.__valorB
        elif self.__operacao == '/':
            if self.__valorB == 0:
                print("Não é possível realizar divisão por zero.")
                exit()
            return self.__valorA / self.__valorB

    def mostrarResultado(self):
        resultado = self.calcular()
        print(f"{self.__valorA} {self.__operacao} {self.__valorB} = {resultado}")

