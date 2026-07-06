valor = float(input('Valor total da compra: R$ '))
valor_pago = float(input('Valor total pago: R$ '))
troco = valor_pago - valor
nota_50 = troco // 50
resto_50 = troco % 50
nota_20 = resto_50 // 20
resto_20 = resto_50 % 20
nota_10 = resto_20 // 10
resto_10 = resto_20 % 10
nota_5 = resto_10 // 5
resto_5 = resto_10 % 5
print('Troco: R${:.2f}'.format(troco))
print('Notas de R$50: {:.0f}'.format(nota_50))
print('Notas de R$20: {:.0f}'.format(nota_20))
print('Notas de R$10: {:.0f}'.format(nota_10))
print('Notas de R$5: {:.0f}'.format(nota_5))
