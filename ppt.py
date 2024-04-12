'''
Lembrando de que seu programa deverá cumprir os seguintes requisitos:
Treinamento Pythonista Autodidata -
1. Permitir que o usuário digite seu nome
2. Permitir que o usuário escolha uma opção entre pedra, papel ou tesoura
3. Exibir o resultado do jogo(perdeu, ganhou ou empatou)
4. Permitir o jogador jogar quantas vezes quiser
'''
jogo = ['Pedra','Papel','Tesoura']
import random

nome = input('Digite seu nome:')
print('-------------------------------------')
print(f'Olá {nome}\nBem Vindo ao Pedra, Papel e Tesoura')
print('Para fechar o jogo, basta digitar "sair"')
print('-------------------------------------')
def ppt():
    while True:
        escolha = input(f'{nome}, escolha entre pedra, papel ou tesoura:')
        bot = (random.choice(jogo))
        if escolha == 'sair':
            print('O jogo foi encerrado com sucesso\nObrigado por Jogar!')
            break
        if bot == escolha:
            print(f'EMPATE: {nome} escolheu {escolha} e o adversário escolheu {bot}!')
        elif bot == 'Papel' and escolha == 'Tesoura':
            print(f'VITÓRIA: {nome} escolheu {escolha} e o adversário escolheu {bot}!')
        elif bot == 'Tesoura' and escolha == 'Papel':
            print(f'DERROTA: {nome} escolheu {escolha} e o adversário escolheu {bot}!')
        elif bot == 'Tesoura' and escolha == 'Pedra':
            print(f'VITÓRIA: {nome} escolheu {escolha} e o adversário escolheu {bot}!')
        elif bot == 'Pedra' and escolha == 'Tesoura':
            print(f'DERROTA: {nome} escolheu {escolha} e o adversário escolheu {bot}!')
        elif bot == 'Pedra' and escolha == 'Papel':
            print(f'VITÓRIA: {nome} escolheu {escolha} e o adversário escolheu {bot}!')
        elif bot == 'Papel' and escolha == 'Pedra':
            print(f'DERROTA: {nome} escolheu {escolha} e o adversário escolheu {bot}!')
        
ppt()





    
