print('''''''''''')
print('Jogo da Advinhação')
print('''''''''''')
palavra_secreta='banana'
chute=str(palavra_secreta)
posição=str(palavra_secreta)
letra=str
acertou=False
errou=False
while (not acertou and not errou):
    print('jogando')
    chute=input('digite uma letra: \n') 
    posição=0
    for letra in palavra_secreta:
        if chute==letra:
           print('encontrei a letra {} na posição {}'.format(letra,posição))
           break
        posição=posição+1
        
    
