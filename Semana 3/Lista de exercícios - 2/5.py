'''
Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima 

'''
num1 = int(input(""))
num2 = int(input(""))
num3 = int(input(""))

if (num1 < num2 and num1 < num3 and num2 < num3):
    print("crescente")
else:
    print("não está em ordem crescente")
