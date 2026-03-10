import random

numero = random.randint(1, 10) # Gera um inteiro entre 1 e 10
chute = ''

while chute != numero:
    try:
        chute = int(input('Chute um numero inteiro aleatório de 1 a 10: '))
        if chute > 10 or chute < 1:
            print('Sabe ler não irmão?')
        elif chute > numero:
            print('Chutou alto')
            print('Tente novamente')
        elif chute < numero:
            print('Chutou baixo')
            print('Tente novamente')
        elif chute == numero:
            print('Acertoouuuu')

    except ValueError:
        print('Insira um valor válido')