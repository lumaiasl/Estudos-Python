total = 1
valor = int(input('Insira um número que deseja calcular o fatorial: '))
if valor > 0:
    for valores in range(1, valor + 1):
        total = total * valores
    print(total)
else:
    print('Valor inválido')