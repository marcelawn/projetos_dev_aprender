'''
eu mostro um exemplo de como esse programa deve funcionar. A ideia geral
é que você inicie um programa que mostra na tela do console 2 opções: 1 - fazer login ou 2 cadastrar novo usuário. Eu
espero que armazene estes dados de login em um arquivo de texto (.txt).
Seu programa deve permitir que :
● Novos usuários sejam criados
○ Novos usuário deveram ser criados e armazenados dentro de um arquivo .txt
● Seja possível efetuar o login
○ O login deve ser efetuado somente quando usuário e senhas estiverem corretos(com base
no arquivo de .txt)
● Quer incrementar ou adicionar novas funcionalidades? Ótimo, quanto mais praticar melhor ficará!'''
from getpass import getpass


print(f'Olá, bem-vindo ao nosso sistema!\nEscolha uma opção\n[1] - Fazer login\n[2] - Cadastrar usuário')
try:
    opcao = input('Digite a opção desejada:')
except ValueError as erro:
    print('Digite apenas valores numéricos!')
if opcao == '2':
    usuario = input('Digite um nome para seu usuário:')
    senha = getpass('Digite uma senha:')
    with open ('usuarios.txt','w',newline='') as arquivo:
        arquivo.write(usuario + ',' + senha)
        print(f'Usuário {usuario}, foi criado com sucesso!')
elif opcao == '1':
    usuario = input('Digite seu usuário:')
    senha = getpass('Digite sua senha:')
    with open ('usuarios.txt','r') as arquivo:
        for linha in arquivo:
            login = linha.split(',')
            if login[0] != usuario or login[1] != senha:
                print('Usuario não existe!')
            elif login[0] == usuario and login[1]  == senha:
                print(f'Bem-vindo {usuario}, seu login foi realizado com sucesso!')
            
  

        
        

    
   

    

    