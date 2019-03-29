'''Nesse programa ele pressupos q a resposta ja era SIM '''
'''quando tem variaveis iguais voic pode colocar elas em linha e igualando-as'''
'''print("Você digitou {} numeros e a media deles foi de {}".format(quant, media)) '''
#aki o {} no meio da frase quer dizer q uma variavel ir vir no lugar especifico e o ". format(variavel A, variavel B)"

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input("Digite um numero: "))
    soma +=num
    quant += 1
    if quant == 1 :
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar a digitar ? [N/S]")).upper().strip()[0]
media = soma / quant
print("Você digitou {} numeros e a media deles foi de {}".format(quant, media))
print("O maior valor que voce digitou foi o {} e o menor valor que você digitou foi o {}" .format(maior, menor))