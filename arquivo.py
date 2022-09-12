print('xxxxxxxxxx')
print('joguinho')
print('xxxxxxxxxx')
numero_secreto='55'
chute=int(numero_secreto)
print('vamos ver se voce sabe qual e o numero que eu quero')
chute=input('digite um numero: \n')
print('voce digitou', chute)
acertou=chute==numero_secreto
errou=chute<numero_secreto
if acertou:
    print('correto')
elif errou:
    print('errou')
print('************')
print('By Felipe')
print('************')
