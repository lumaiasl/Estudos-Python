preços = [12, 14, 22, 32, 33, 55, 63]

# índice primeiro item da lista [0]    
print(preços[0])

# índice terceiro item da lista [2] 
print(preços[2])

# encontrar índice automaticamente
print(preços.index(33))

# manipular - adicionar item
idades = [23, 53, 24, 18]

idade_usuario = int(input('Qual é a sua idade? '))
idades.append(idade_usuario)
print(idades)

# dado uma lista de números, some o valor total

n = [2, 34, 54, 12, 7, 88, 92, 1]
total = 0
for numero in n:
    total = total + numero
print(total)