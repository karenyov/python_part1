'''
Exercício 2
Este é o desafio do vídeo "Entrada de Dados".

Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja,
faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias,
horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos.
Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:

Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:
2 dias, 1 horas, 36 minutos e 55 segundos.

'''

s = int(input("Por favor, entre com o número de segundos que deseja converter: "))

a = s//60//60//24
b = (s//60//60)%24
c = (s//60)%60
d = s%60

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")
