'''
Exercício 2 - Desafio da videoaula
Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de
uma equação do segundo grau.


O programa deve receber os parâmetros  a a,  b b, e  c c da equação  ax^2 + bx + c ax 
2
 +bx+c, respectivamente, e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:

a raiz desta equação é X

ou

a raiz dupla desta equação é X

onde X é o valor da raiz dupla

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente. Exemplos:

as raízes da equação são 1.0 e 2.0

as raízes da equação são -2.0 e 0.0

'''
import math

a = float(input(""))
b = float(input(""))
c = float(input(""))

delta = b ** 2 - 4 * a  * c

if delta == 0:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é",r1)

else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        r1 = (-b + math.sqrt(delta)) / (2 * a)
        r2 = (-b - math.sqrt(delta)) / (2 * a)

        if (r1 == r2):
            print("a raiz dupla desta equação é",r1)
        elif (r1 > r2):
            print("as raízes da equação são",r2,"e",r1)
        else:
            print("as raízes da equação são",r1,"e",r2)





