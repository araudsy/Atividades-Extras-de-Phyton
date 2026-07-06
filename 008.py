capital = float(input('Qual o capital? '))
taxa = float(input('Qual é a taxa de juros? '))
tempo = float(input('Quantos meses? '))
taxa_decimal = taxa / 100
montante_final = capital * (1 + taxa_decimal * tempo)
print('O montante final é de {:.2f}'.format(montante_final))
