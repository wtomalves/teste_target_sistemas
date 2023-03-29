import json

with open("faturamento.json", encoding='utf-8') as dados_json:
    dados = json.load(dados_json)


#print(dados)

print("\nRelatório: \n")

maior_faturamento = 0
menor_faturamento = 0
dia_maior_faturamento = 0
dia_menor_faturamento = 0
media_faturamento = 0
valor_total = 0
dias_de_faturamento = 0
dias_acima_da_media = []

for i in dados:
    dia = i['dia']
    valor = float(i['valor'])
    valor_total = valor_total + valor

    "Maior faturamento"
    if maior_faturamento < valor:
        maior_faturamento = valor
        dia_maior_faturamento = dia
        if menor_faturamento == 0:
            menor_faturamento = maior_faturamento

    "Menor faturamento"
    if menor_faturamento > valor and valor > 0:
        menor_faturamento = valor
        dia_menor_faturamento = dia

    "Contagem de dias de faturamento excluindo sabado domingo e feriado"
    if valor != 0:
        dias_de_faturamento = dias_de_faturamento + 1

    media_faturamento = valor_total / dias_de_faturamento

    if valor > media_faturamento:
        dias_acima_da_media.append(dia)


print("*" * 110)
print("O maior faturamento ocorreu no dia", dia_maior_faturamento, "no valor de", maior_faturamento)
print("O menor faturamento ocorreu no dia", dia_menor_faturamento, "no valor de", menor_faturamento)
print("Valor total:", valor_total)
print("Dias de faturamento excluindo sábados, domingos e feriados: ", dias_de_faturamento, "dias.")
print("Media faturamento:", media_faturamento)
print("Dias em que o valor de faturamento foi maior que a média:", dias_acima_da_media, "totalizando:",
      len(dias_acima_da_media), "dias.")

print("*" * 110)

