faturamento = 5000
custo = 2900
novas_vendas = 300

faturamento = faturamento + novas_vendas #Soma
taxa_imposto = 0.1
imposto = taxa_imposto * faturamento #Multiplicação

lucro = faturamento - custo - imposto #Subritair

print(faturamento)
print(lucro)

margem_lucro = lucro / faturamento #Divisao
print(margem_lucro)

restituicao = imposto * 0.1
print(restituicao)

tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12)
print(tempo_em_anos, "anos")
print(tempo_em_meses % 12, "meses")
