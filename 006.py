distancia = float(input('Qual é a distância em km? '))
consumo = float(input('Quantos km/l? '))
total = distancia / consumo
print('Serão necessários {:.2f} litros.'.format(total))
