

print("\nsao_paulo = R$67836.43, "
      "\nrio_de_janeiro = R$36678.66, "
      "\nminas_gerais = R$29229.88, "
      "\nespiritp_santo = R$27165.48, "
      "\noutros = R$19849.53"

)

sao_paulo = 67836.43
rio_de_janeiro = 36678.66
minas_gerais = 29229.88
espiritp_santo = 27165.48
outros = 19849.53
soma = sao_paulo + rio_de_janeiro + minas_gerais + espiritp_santo + outros

print("Valor total do faturamento mensal R$", soma, "\n")

print("Calculando o percentual de representação de cada e estado\n")

print("São paulo corresponde a", (sao_paulo * 100) / soma,"%")
print("Rio de Janeiro  corresponde a", (rio_de_janeiro * 100) / soma,"%")
print("Minas Gerais corresponde a", (minas_gerais * 100) / soma,"%")
print("Espirito Santo corresponde a", (espiritp_santo * 100) / soma,"%")
print("Outros estados corresponde a", (outros * 100) / soma,"%")
