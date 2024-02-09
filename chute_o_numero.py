'''
Neste projeto, você deverá criar um programa que irá gerar um número dentro de uma faixa (ex: 1 a 100). Além disso o
programa deverá permitir que o usuário chute o valor até que ele acerte. Seu programa deverá dar dicas sobre quão
próximo o valor digitado foi ao valor que foi realmente gerado pelo seu programa. Finalmente o usuário deverá ser
oferecido a opção de jogar novamente, se quiser.

Lembrando de que seu programa deverá cumprir os seguintes
requisitos:
1. Exiba alguma mensagem de apresentação, que apresenta seu programa para o usuário
2. O jogo deverá iniciar somente após o jogador(a) apertar “enter” no teclado (dica de como fazer isso
aqui)
3. O número gerado não deve ser exibido para o jogador(a).
4. O jogador(a) deve ser capaz de chutar quantas vezes necessário.
5. Seu código deve tratar as possíveis exceções que possam ser geradas pelo jogador(a).
6. Caso o jogador(a) erre o chute, dê dicas se ele(a) deve chutar mais alto ou mais baixo.
7. Ao acertar o chute, ofereça ao jogador(a) a opção de jogar novamente
'''

'''
1º Passo - Gerar um número aleatorio e guardar essa informação em uma variavel
2° Passo - Solicitar um chute para o jogador
3° Passo - Caso o jogador erre, imprimir na tela se o número gerado é maior ou menor do que o numero chutado
4° Passo - Repetir o processo até que o jogador acerte
5° Passo - Caso o jogador acertar, exibir uma mensagem de acerto junto ao numero gerado 
6° Passo - Perguntar ao jogador se ele deseja jogar de novo, caso sim, continuar o jogo, caso contrario, encerrar o programa.
'''
import random
valor_aleatorio = (random.randint(1,100))
nome = input('Digite seu nome: ')
print('---------------------------------')
print(f'Olá {nome}, bem vindo ao jogo Chute o Número!')
print('---------------------------------')
input('Aperte enter para começar...')
print('---------------------------------')
def chute_numero():
    while True:
        try:
            numero_chutado = int(input('Chute um número de 1 a 100: '))
        except ValueError as erro:
            print('Por favor digite apenas números!')
        

        if numero_chutado > valor_aleatorio:
            print('Chute um número menor!')
        elif numero_chutado < valor_aleatorio:
            print('Chute um número maior!')
        else: 
            print(f'PARÁBENS! VOCÊ ACERTOU O NÚMERO {valor_aleatorio} ')
            processo = input('Deseja continuar jogando? (s/n)')
            if processo.lower() not in 's':
                print('Jogo finalizado!')
                break
            else:
                continue

chute_numero()