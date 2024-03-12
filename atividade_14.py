from os import system

system('cls')

def l():
    print('=-'*15)
l()
print('     calculador de peso')
l()

peso_kg = float(input("Digite o seu peso em kg: "))
novo_peso = peso_kg * 0,15
novo_peso = float(novo_peso)
peso_kg = peso_kg + novo_peso

print(f"O peso caso a pessoa engorde, vai ser {peso_kg}")

novo_peso = peso_kg * 0,20
peso_kg = peso_kg - novo_peso

print(f"O peso caso a pessoa perca, vai ser {peso_kg}")