segundos_totais = int(input('Digite a quantidade de segundos: '))
total_original = segundos_totais
horas = segundos_totais // 3600
segundos_totais = segundos_totais % 3600
minutos = segundos_totais // 60
resto_minutos = segundos_totais % 60
print('{} segundos equivalem a {}h {}min {}s'.format(total_original, horas, minutos, resto_minutos))
