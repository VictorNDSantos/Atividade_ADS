from os import system

system('cls')

def l():
    print('=-'*11)
l()
print('     calculador:')
l()

np = int(input("digite um numero maior que 0: "))

while np <= 0:
    print("Digite o numero maior que zero!!")
    np = int(input("digite um numero maior que 0: "))

nd = np ** 2
rq = np**(1/2)
print(f"O numero {np} digitado ao quadrado é {nd} ")
print(f"O numero {np} a raiz quadrada é {rq:.0f} ")