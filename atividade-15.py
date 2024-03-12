from os import system

system('cls')

def l():
    print('=-'*15)
l()
print('     calculador de contas')
l()

salario = float(input("Digite o valor do salário: "))

c1 = float(input("Digite o valor da primeira conta: "))
c2 = float(input("Digite o valor da segunda conta: "))

c1_com_juros = c1 * 1.02
c2_com_juros = c2 * 1.02

restante_sal = salario - (c1_com_juros + c2_com_juros)

print(f"O valor da primeira conta com juros é: {c1_com_juros}")
print(f"O valor da segunda conta com juros é: {c2_com_juros}")
print(f"O valor restante do salário é: {restante_sal}")