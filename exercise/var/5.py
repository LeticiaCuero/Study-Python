# Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)
# Cenário: Um contrato de manutenção de software tem a duração de 40 meses. 
# O cliente quer ver esse tempo no formato: "X anos e Y meses". 
# Objetivo: Utilize os operadores de divisão inteira e resto da divisão para converter os 40 meses.

m = 40

anos = m // 12
meses = m % 12

print(f"O contrato tem a duração de: {anos} anos e {meses} meses")
