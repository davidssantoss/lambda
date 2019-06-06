"""
@author: David S
1. Usando map extraer de una lista de listas el primer y ultimo elemento de cada
lista
2. Dada una lista de numeros entreros, usando map y filter retornar una lista con
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
lista = [[1,2,3],[54,5]]
uno = list(map(lambda x: x[0], lista))
ultimo = list(map(lambda x: x[-1], lista))
print(uno + ultimo)
