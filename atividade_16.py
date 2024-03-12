from os import system

system('cls')

def l():
    print('=-'*24)
l()
print('     calculador de pontencia de iluminação')
l()

eficacia_luminosa = int(input('Digite a eficácia luminosa da lâmpada: '))

potencia_lampada_watts = int(input('Digite a potência da lâmpada em watts: '))

potencia_lampada_lumens = eficacia_luminosa * potencia_lampada_watts

iluminacao_desejada_lux = int(input("Digite a iluminação em lux: "))

comprimento_m = int(input('Digite o comprimento do comodo em metros: '))
largura_m = int(input('Digite a largura do comodo em metros: '))

area_m2 = comprimento_m * largura_m

potencia_necessaria_lumens = iluminacao_desejada_lux * area_m2

quantidade_lampadas = potencia_necessaria_lumens / potencia_lampada_lumens

print(f'Você precisará de {quantidade_lampadas:.0f} lâmpadas.')