from os import system

system('cls')

def l():
    print('=-'*11)
l()
print('     calculador de ração:')
l()

peso_saco = float(input("Digite o peso do saco em kg: "))
quant_racao = float(input("Digite a media de ração que gato come por dia: "))

peso_q = peso_saco * 1000
print(peso_q)
quant_racao = quant_racao * 2
quant_racao = quant_racao * 5
quant_result = quant_racao - peso_q

print(f"A quantidade de ração restante é {quant_result:.0f} ")