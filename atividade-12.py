from os import system

system('cls')

def l():
    print('=-'*13)
l()
print('     media das notas')
l()

nota_1 = float(input("Digite o valor da primeira nota: "))
nota_2 = float(input("Digite o valor da segunda nota: "))
nota_3 = float(input("Digite o valor da terceira nota: "))

nota_1 = nota_1 * 2
nota_2 = nota_2 * 3
nota_3 = nota_3 * 5

media = (nota_1 + nota_2 + nota_3)/ 10

l()
print(f'A Media final do Aluno é: {media}')