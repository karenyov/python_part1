'''

Exercício 3
Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.
Observe o exemplo abaixo:

Exemplo 1:

Entrada de Dados:

Digite um número inteiro: 78615

Saída de Dados:

O dígito das dezenas é 1

Exemplo 2:

Entrada de Dados:

Digite um número inteiro: 2

Saída de Dados:

O dígito das dezenas é 0

'''

n = int(input("Digite um número inteiro: "))

d = (n % 100) // 10 
print("O dígito das dezenas é",d)
