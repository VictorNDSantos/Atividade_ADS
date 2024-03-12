def l():
    print('=-'*30)
l()
print('     convertor de segundos em minutos e segundos:')
l()

s = float(input("Quantos segundos vc deseja adicionar: "))
m = s//60
seg_restantes = s % 60
print(f"o resultado é {m:.0f}:{seg_restantes:.0f}")