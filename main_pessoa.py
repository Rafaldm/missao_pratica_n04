from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

# Criando instâncias e imprimindo dados

# Instância de Pessoa
pessoa = Pessoa("Rafael Lima", "12345", "18-05-1995", "Ativa")
pessoa.imprimir_dados()

# Instância de PessoaFisica
pessoa_fisica = PessoaFisica("Mateus Oliveira", "54321", "2015-05-15", "Ativa", "1990-07-22", "12345678901", "MG-12.345.678")
pessoa_fisica.imprimir_dados()

# Instância de PessoaJuridica
pessoa_juridica = PessoaJuridica("Empresa MAXLINE Ltda", "67890", "2020-11-20", "Ativa", "2018-09-10", "12.345.678/0001-95")
pessoa_juridica.imprimir_dados()

# Alterar valores via setter
try:
    pessoa_fisica.cpf = "1234567890"  # Valor inválido
except ValueError as e:
    print(e)

try:
    pessoa_juridica.cnpj = "12.345.678/0001-9"  # Valor inválido
except ValueError as e:
    print(e)

# Alterar para valores válidos
pessoa_fisica.cpf = "12345678901"  # Valor válido
pessoa_juridica.cnpj = "12.345.678/0001-95"  # Valor válido
