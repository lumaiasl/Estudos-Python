# validador do tamanho de senhas

senhas = ["123","avs","dwaswe","1252123"]
for senha in senhas:
    if len(senha) >= 6:
        print("validou")
    else:
        print("não validou")

senha1 = input('Digite uma senha com mais de 6 caracteres: ')

while len(senha1) < 6:
        senha1 = input('Tente novamente:')

print('Senha válida')

# validador de login kkkkkkkk
tentativas = 0
usuario = input('insira seu usuário: ')
senha = input('insira sua senha: ')

def login():
    global tentativas
    usuario1 = input('Confirme seu usuário: ')
    senha1 = input('Confirme sua senha: ')
    
    def confirme():
        global tentativas
        if tentativas >= 3:
            print('Tente novamente mais tarde')
        elif usuario1 != usuario or senha1 != senha:
            print('Tente novamente')
            tentativas +=1
            if tentativas == 1:
                print(f'você utilizou {tentativas} tentativa')
            else:
                print(f'você utilizou {tentativas} tentativas')
            login()

        elif usuario1 == usuario or senha1 == senha:
            print('pabens')

    confirme()

login()

# validador de login com while agora

tentativas = 0
usuario = input('insira seu usuário: ')
senha = input('insira sua senha: ')
usuario1 = ''
senha1 = ''

while usuario != usuario1 or senha != senha1 and tentativas < 3:
    usuario1 = input('confirme seu usuário: ')
    senha1 = input('confirme sua senha: ')
    tentativas +=1
    if tentativas == 1:
        print(f'você utilizou {tentativas} tentativa')
    else:
        print(f'você utilizou {tentativas} tentativas')

if usuario == usuario1 and senha == senha1:
    print('pabens')

else:

    print('tente novamente mais tarde')
