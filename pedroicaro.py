# Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.
TERMO = int(input("Digite o primeiro termo da PA: "))
RAZAO= int(input("Digite a razão da PA: "))
for i in range(10):
    print(i)
    termo = TERMO + i * RAZAO
    print(f'''Termo {i+1}-{termo}''')