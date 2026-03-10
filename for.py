# Laços de repetição

# Range nunca inclui o último número, vai até 10
for item in range(1,11):
    print(item)

# Range imprime números de 2 até 10 de 2 em 2
for item in range(2,12,2):
    print(item)

# Listas
nomes = ["João","Amanda","Rafael"]

# lista variáveis diferentes
dados = [1,"Jonas",True,2.3]

for nome in nomes:
    print(nome)

for dado in dados:
    print(dado)


idades = [12,32,16,18,21,25]

# exiba os maiores de idade na tela
for idade in idades:
        if idade >= 18:
            print(f'{idade} é maior de idade')
        else:

            print(f'{idade} é menor de idade')
