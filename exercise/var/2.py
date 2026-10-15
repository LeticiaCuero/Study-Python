# Exercício 2: Controle de Estoque de E-commerce (Logística)
# Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no estoque. 
# Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um fornecedor. 
# Objetivo: Atualize a variável de estoque e exiba o saldo final. 

smartphone = 250
vendas = 78
fornecedor = 100

saldo = smartphone - vendas + fornecedor

smartphone = saldo

print(f"O saldo final de smartphones em estoque é: {smartphone} unidades")