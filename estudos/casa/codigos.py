faturamento = 5000
custo = 2900

novas_vendas = 300
faturamento = faturamento + novas_vendas

taxa_imposto = 0.1
imposto = taxa_imposto * faturamento


print('Faturamento',faturamento)
print('Custo',custo)
print('Lucro',faturamento - custo - imposto)
