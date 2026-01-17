"""
UNIVERSIDAD DEL VALLE DE GUATEMALA
TEORIA DE PROBABILIDADES
LABORATORIO 01: Análisis Combinatorio
Angel Gabriel Chavez Otzoy
Esteban Emilio Cumatz Quiná
Joel Josué Nerio Alonzo</div>
José Leonel Rivera Barrera
Luis Adrian Estrada
"""
import itertools as iter

#-------------------------EJERCICIO 1-----------------

#Digitos
N=[]
for i in range(10):
    N.append(i)

A=list(iter.product(N,repeat=4))


#1) Contar Suceciones donde se vale repetir
def sucesionesNormal(N,r):
    result=len(A)
    return result

#1) Sucesion de 4 dígitos diferentes
def sucesionesDiferentes(N, r):
    A = list(iter.permutations(N, r))
    result = len(A)
    return result

#2)Sucesiones con uno o más dígitos repetidos
def sucesionRepetidos(N,r):
    total=sucesionesNormal(N,r) - sucesionesDiferentes(N,r)
    return total

#3.1)Todos repetidos
def sucesionesTodosRepetidos(A):
    contador = 0
    for s in A:
        # Comparamos si todos los elementos son iguales al primero
        if s[0] == s[1] == s[2] == s[3]:
            contador += 1
    return contador

#3.2)Se repiten 2 dígitos 2 veces cada uno
def sucesionesDoblePareja(lista):
    contador = 0
    for s in lista:
        # 1. Convertimos la tupla a set para ver cuántos dígitos distintos hay
        distintos = set(s)

        # 2. Si hay exactamente 2 dígitos distintos...
        if len(distintos) == 2:
            # 3. Verificamos que sea "Doble Pareja" (2 y 2) y no "Trío" (3 y 1)
            # Tomamos cualquiera de los dos dígitos y contamos cuántas veces aparece
            primer_digito = list(distintos)[0]

            if s.count(primer_digito) == 2:
                contador += 1

    return contador



#3.3)una única pareja
def sucesionUnicaPareja(lista):
    contador = 0
    for s in lista:
        # 1. Convertimos la tupla a set para ver cuántos dígitos distintos hay
        distintos = set(s)

        if len(distintos) == 3:
            contador += 1
    return contador


#3.4)se repite un dígito tres veces
def sucesionTresRepetidos(lista):
    contador = 0
    for s in lista:
        # 1. Convertimos la tupla a set para ver cuántos dígitos distintos hay
        distintos = set(s)

        if len(distintos) == 2:
            numero_a_probar = list(distintos)[0]

            if s.count(numero_a_probar) == 3 or s.count(numero_a_probar) == 1:
                contador += 1
    return contador

#-----------------EJERCICIO 2-------------------------------------

#Encontrar numeros primos usando el principio de inclusion y exclusion
numeros_primos = [2]
todo = 100
numeros = [i for i in range(1,101,2)]
C1 = [i for i in numeros if i % 7 == 0 and i != 7 ]
C2 = [i for i in numeros  if i % 3 == 0 and i != 3]
C3 = [i for i in numeros if i % 5 == 0 and i != 5]


def interseccion (multiplos1,multiplos2):
    """Esta función reune los múltiplos en común"""
    interseccion = []
    for i in multiplos1 and multiplos2:
        if i in multiplos1 and multiplos2:
            interseccion.append(i)
    return interseccion

N1 = interseccion(C1,C2)
N2 = interseccion(C2,C3)
N3 = interseccion(C1,C3)

#Encontrar los numeros primos
for i in numeros:
    if i not in C1 and i not in C2 and i not in C3 and i != 1:
        numeros_primos.append(i)
    else:
        continue

#-----------------PARTE 3-------------------------------------
n = 7
m = 5
k = 0


conjunto_tuplas = set() #esto va a ser el conjunto de tuplas generadas por los val de las var i

for i1 in range(1, n+1):
    for i2 in range(1, i1+1):
        for i3 in range(1, i2+1):
            for i4 in range(1, i3+1):
                for i5 in range(1, i4+1):
                    k = k + 1
                    # Agregar la tupla al conjunto pero cabal con el orden establecido
                    conjunto_tuplas.add((i5, i4, i3, i2, i1))

# Generar muestras de 5 elementos de 7 elementos con remplazo
muestras_con_remplazo = set(iter.combinations_with_replacement(range(1, 8), 5)) # este es el conjunto  de las muestras de 5 elementos  de 7  elementos con remplazo

print(f"""
=================================
PARTE 1
=================================

a. Contar una sucesión de 4 dígitos
Tiene como resultado: {sucesionesNormal(N,4)} posibles combinaciones.
El Resultado de 4 dígitos distintos en una sucesión es: {sucesionesDiferentes(N,4)}.

b. Sucesiones con uno o más dígitos repetidos
Una sucesión con al menos un repetido tiene: {sucesionRepetidos(N,4)} posibilidades.

c. Conteo de elementos por cada una de las siguientes divisiones, 
  utilizando la generación que realizó en el inciso b):

c.1. Todos repetidos
Una suseción con todos los dígitos repetidos es de: {sucesionesTodosRepetidos(A)} posibilidades.

c.2. Se repiten 2 dígitos 2 veces cada uno
Una sucesión con 2 parejas de números tiene: {sucesionesDoblePareja(A)} resultados.

c.3. una única pareja
Una sucesión con una única pareja tiene: {sucesionUnicaPareja(A)} resultados.

c.4. se repite un dígito tres veces
Una sucesión con tres dígitos repetidos es: {sucesionTresRepetidos(A)}.

=================================
PARTE 2
=================================
Encontrar numeros primos usando el principio de inclusion y exclusion
Sucesión de primos: {numeros_primos}
Coneteo: {len(numeros_primos)}
      
=================================
PARTE 3
=================================

Valor de k: {k}
Número de tuplas en el conjunto: {len(conjunto_tuplas)}
Número de muestras con remplazo: {len(muestras_con_remplazo)}

¿Son iguales los conjuntos? {conjunto_tuplas == muestras_con_remplazo}
      
Las combinaciones con repetición de 5 elementos tomados de {1,2,3,4,5,6,7}, que son {len(muestras_con_remplazo)} en total.
""")
