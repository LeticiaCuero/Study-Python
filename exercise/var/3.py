# Exercício 3: Divisão de Cargas (Logística/Transporte)
# Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. 
# Cada caminhão suporta exatamente 12 caixas. 
# Objetivo: 1. Quantos caminhões sairão totalmente cheios? (Use //) 
# 2. Quantas caixas sobrarão para serem enviadas em uma última viagem menor? (Use %)

t = 1250
c = 12

total = t / c
sobras = t % c

print(f"Total de caminhões totalmente cheios: {total:.0f}")
print(f"Total de caixas que sobrarão para a última viagem: {sobras}")