# Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)
# Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a equipe de vendas. 
# Objetivo: Calcule o valor do bônus e o faturamento final da empresa após subtrair esse bônus.
#●	Faturamento inicial: 50.000
#●	Percentual de bônus: 0.10

bonus = 0.10
faturamento = 50000

final = faturamento * bonus + faturamento

print(f"O valor do bônus é: R$ {final:.2f}")
