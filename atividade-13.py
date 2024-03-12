from os import system

system('cls')

def l():
    print('=-'*15)
l()
print('     custo do espetaculo')
l()

custo_espetaculo = float(input("Digite o custo total do espetaculo: "))
preco_convite = float(input("Digite o preço do convite: "))

vendas = custo_espetaculo / preco_convite
print(f"A quantidade de convites que deve ser vendidos é: {vendas:.0f}")