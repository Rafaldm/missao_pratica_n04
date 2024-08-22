from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, numero_conta, data_abertura_conta, status, data_abertura_empresa, cnpj):
        super().__init__(nome, numero_conta, data_abertura_conta, status)
        self.__data_abertura_empresa = data_abertura_empresa
        self.__cnpj = cnpj

    @property
    def data_abertura_empresa(self):
        return self.__data_abertura_empresa

    @data_abertura_empresa.setter
    def data_abertura_empresa(self, valor):
        self.__data_abertura_empresa = valor

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, valor):
        if len(valor) == 18:
            self.__cnpj = valor
        else:
            raise ValueError("CNPJ deve ter 18 caracteres.")
