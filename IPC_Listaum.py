# Lista 1 - Introdução a Programação de Computadores

# Prof. Breno Gabriel da Silva - UniFEITEP - 2026

# ===================== EXERCICIO 1 - print() =====================

# a) mensagem simples

print(“Olá, mundo da programação!”)

# b) nome completo

print(“Gustavo”)

# c) três informações em linhas separadas

print(“Introdução a Programação de Computadores”)
print(“Gustavo”)
print(“Estou aprendendo Python!”)

# d) pequena apresentação

print(“Gustavo”)
print(“20 anos”)
print(“Maringá”)
print(“Engenharia de Software”)

# ===================== EXERCICIO 2 - variáveis =====================

# a) variáveis sobre um filme

filme = “Interestelar”
ano_lancamento = 2014
nota_filme = 9.5

print(filme)
print(ano_lancamento)
print(nota_filme)

# b) variáveis de um produto

nome_produto = “Teclado Mecânico”
preco = 350.00
quantidade_estoque = 12

print(nome_produto)
print(preco)
print(quantidade_estoque)

# c) informações de um aluno em frases completas

nome_aluno = “Gustavo”
turma = “CC1A”
media_final = 8.7

print(“O nome do aluno é”, nome_aluno)
print(“A turma é”, turma)
print(“A média final é”, media_final)

# d) informações de uma viagem

destino = “Florianópolis”
quantidade_dias = 7
valor_passagem = 620.00
meio_transporte = “avião”

print(destino)
print(quantidade_dias)
print(valor_passagem)
print(meio_transporte)

# ===================== EXERCICIO 3 - type() =====================

# a) verificando o tipo de valores diretos

print(type(“Python”))
print(type(2026))
print(type(3.14))
print(type(False))

# b) quatro variáveis de tipos diferentes

texto = “olá”
inteiro = 42
decimal = 3.14
logico = True

print(type(texto))
print(type(inteiro))
print(type(decimal))
print(type(logico))

# c) testando tipos e observando a diferença entre numero e texto

print(type(“123”))   # isso é str mesmo parecendo número
print(type(123))     # aqui sim é inteiro
print(type(12.3))
print(type(True))

# d) variáveis sobre uma cidade

cidade = “Maringá”
habitantes = 1900000
temperatura_media = 17.5
esta_chovendo = False

print(type(cidade))
print(type(habitantes))
print(type(temperatura_media))
print(type(esta_chovendo))

# ===================== EXERCICIO 4 - conversão de dados =====================

# a) convertendo texto para inteiro

idade_texto = “18”
idade_int = int(idade_texto)
print(idade_int)
print(type(idade_int))

# b) convertendo texto para float

preco_texto = “59.90”
preco_float = float(preco_texto)
print(preco_float)
print(type(preco_float))

# c) convertendo inteiro para string

numero = 100
numero_texto = str(numero)
print(numero_texto)
print(type(numero_texto))

# d) convertendo duas strings para int e float

string_inteiro = “45”
string_decimal = “7.8”

convertido_int = int(string_inteiro)
convertido_float = float(string_decimal)

print(convertido_int)
print(type(convertido_int))
print(convertido_float)
print(type(convertido_float))