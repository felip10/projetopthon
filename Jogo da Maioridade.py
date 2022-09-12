print('xxxxxxxxxxxxxxxxxxxxx')
print('Jogo da Maioridade')
print('xxxxxxxxxxxxxxxxxxxxx')


idade_maior='18'
idade=int(idade_maior)
numero_de_tentativas=3
rodada=1
while(numero_de_tentativas>0):
 idade=input('digite sua idade: \n')
if idade>=idade_maior:
    print('voce é maior de idade')
else:
    print('voce é menor de idade')

numero_de_tentativas=numero_de_tentativas-1
