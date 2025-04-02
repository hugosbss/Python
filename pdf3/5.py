# 05) Faça a conversão de um tempo expresso em horas, minutos e segundos para somente em segundos.
horas = float(input ('Digite a quantidade de horas: '))
minutos = float(input ('DIgite a quantidade de minutos: '))
segundos = float (input ('Digite a quantidade de segundos: '))
total = (horas * 3600) + (minutos * 60) + segundos
print ('O total em segundos é: ', total)