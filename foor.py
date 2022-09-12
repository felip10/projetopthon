numero='45'
chute=int(numero)
numero_de_tentativas=3
rodada=1
for rodada in range(1,numero_de_tentativas+1):
    print('tentativa {} de {}'.format(numero_de_tentativas,rodada))
    chute=input('digite um numero: \n')
    print('voce digitou',chute)
    acertou=chute==numero
    if acertou:
        print('muito bem, acertou')
        break
    else:
        print('voce errou')
        print('fim de jogo')

