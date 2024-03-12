def l():
    print('=-'*16)
l()
print('     calculador de salario:')
l()

sm = float(input("Digite o salario minimo: "))
ht = float(input("Digite o valor da hora trabalhada: "))

vh = sm / 2
print(vh)
sb = ht * vh
print(sb)
i = (3/100) * sb
print(i)
sr = sm - i

print(f"O salario a receber é {sr:.2f}")