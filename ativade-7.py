from math import sqrt
def l():
    print('=-'*20)
l()
print('     calcule o triangulo retangulo')
l()

a = float(input("qual o valor do a: "))
b = float(input("qual o valor do b: "))

calcula = a**2 + b**2

c = sqrt(calcula)

print(f"o valor do triangulo retangulo é: {c:.2f}")