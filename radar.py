velocidademaxima = 80
try:
    velocidade = float(input('Insira a velocidade analisada: '))

    if velocidade <= 0:
        print("Insira um valor válido")
    elif velocidade <= velocidademaxima and velocidade >= velocidademaxima * 0.5:
        print("não houve multa")
    elif velocidade < velocidademaxima * 0.5:
        print("Multa média, abaixo da velocidade mínima")
    elif velocidade >= velocidademaxima and velocidade < velocidademaxima * 1.2:
        print('Multa média. acima da velocidade máxima')
    elif velocidade >= velocidademaxima * 1.2 and velocidade < velocidademaxima * 1.5:
        print("Multa grave")
    elif velocidade >= velocidademaxima * 1.5:
        print('Multa gravíssima')
except ValueError:
    print("Insira um valor válido")