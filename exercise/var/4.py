# Exercício 4: Análise de Margem de Lucro (Financeiro)
# Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. 
# Os custos fixos foram de R$ 5.000,00 e o imposto sobre o faturamento é de 15%. 
# Objetivo: Calcule o imposto, o lucro líquido e a margem de lucro (Lucro / Faturamento). 
# No final, crie uma variável booleana chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).

faturamento = 15000
custos = 5000
imposto = 0.15

t_imposto = faturamento * imposto
lucro = faturamento - custos - t_imposto
margem = lucro / faturamento

meta_atingida = margem > 0.30

print(f"Imposto sobre o faturamento: R$ {t_imposto:.2f}")
print(f"Lucro líquido: R$ {lucro:.2f}")
print(f"Margem de lucro: {margem:.2f}")
print(f"Meta atingida: {meta_atingida}")