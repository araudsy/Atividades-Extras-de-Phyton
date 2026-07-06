conta = float(input('Digite o valor da conta: '))
percentual = float(input('Digite o percentual de gorjeta desejado: '))
gorjeta = conta * (percentual / 100)
total = conta + gorjeta
print('O valor  da gorjeta é de {:.2f} e o total da conta é de {:.2f}'.format(gorjeta, total))
