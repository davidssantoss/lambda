"""
@author: David S
1. Usando map extraer de una lista de listas el primer y ultimo elemento de cada
lista
2. Dada una lista de numeros enteros, usando map y filter retornar una lista con
los numeros superpares(Todos los digitos son pares)
3. Usando reduce y map extraer los valores máximos de cada lista de una lista
de listas
4. Usando reduce, map y filter extraer los valores mínimos de cada lista de una
lista de listas que cumplen el concepto de número superpar
5. Usando map y filter retornar de una lista los valores menores a la potencia
5 de la cabeza de la lista
6.usando map, filter y/o reduce dada una lista de tuplas caracterizada por
(int x, int y) sumar los x que cumplan con el criterio de ser el número
triangular de y
"""
from functools import reduce
# Primer ejercicio
lista = [[55,1,2,3],[54,5]]
uno = list(map(lambda x: x[0], lista))
ultimo = list(map(lambda x: x[-1], lista))
print(uno + ultimo)
#Segundo ejercicio
lista2 = [10,5,15,22,33,48]
def superPares(lista):
    x = list(filter(lambda x: x % 2 == 0, lista))
    m = list(map(lambda y: y // 10, x))
    return list(filter(lambda x: x % 2 == 0, m))
    
print(superPares(lista2))
# tercer ejercicio
f = lambda a,b: a if (a > b) else b
x = list(reduce(f, lista))
print(reduce(f, x))
#Cuarto ejercicio
f2 = lambda a,b: a if (a < b) else b


