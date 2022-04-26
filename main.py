import random


"""
Crea la primer solución, una aleatoria

Args:
    tsp: Lista de arrays con la representación del problema del viajero. 
Returns:
    solucion: la primer solución aleatoria
"""
def solucionAleatoria(tsp):
    ciudades = list(range(len(tsp))) #creamos una lista basándonos en la long. del array
    solution = []

    # iteramos la lista de ciudades, representadas en los elementos del array "tsp"
    for i in range(len(tsp)):
        # generamos un número aleatorio, que va desde 0 hasta la long. de la lista - 1
        rnd = random.randint(0, len(ciudades) -1)
        ciudadRandom = ciudades[rnd]
        # agregamos la ciudad aleatoria al array de soluciones
        # como solo se puede visitar 1 ciudad 1 sola vez, la borramos de la lista de ciudades originales
        solution.append(ciudadRandom)
        ciudades.remove(ciudadRandom)
    return solution


"""
Calcula la longitud de una ruta dada

Args:
    tsp: Lista de arrays con la representación del problema del viajero. 
    solution: sol. aleatoria o mejor sol. que podría reemplezar la solución actual
Returns:
    longRuta: la longitud de la ruta
"""
def longRuta(tsp, solution):
    longRuta = 0
    for i in range(len(solution)):
        longRuta += tsp[solution[i - 1]][solution[i]]
    return longRuta


"""
Obtiene posibles soluciones mediante los vecinos cercanos ruta dada

Args:
    solution: sol. aleatoria o mejor sol. que podría reemplezar la solución actual
Returns:
    vecinos: los vecinos :v
"""
def obtenerVecinos(solution):
    vecinos = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            vecinos.append(neighbour)
    return vecinos


"""
Obtiene el mejor vecino

Args:
    tsp: Lista de arrays con la representación del problema del viajero. 
    vecinos: la lista de los vecinos :v
Returns:
    mejorVecino: el mejor vecino
    mejorLongitudDeRuta: la mejor longitud de ruta
    
"""
def obtenerMejorVecino(tsp, vecinos):
    mejorLongitudDeRuta = longRuta(tsp, vecinos[0])
    mejorVecino = vecinos[0]
    for vecino in vecinos:
        actualLongitudDeRuta = longRuta(tsp, vecino)
        if actualLongitudDeRuta < mejorLongitudDeRuta:
            mejorLongitudDeRuta = actualLongitudDeRuta
            mejorVecino = vecino
    return mejorVecino, mejorLongitudDeRuta


"""
Implementación del algoritmo de ascensión de colinas

Args:
    tsp: Lista de arrays con la representación del problema del viajero. 
    vecinos: la lista de los vecinos :v
Returns:
    mejorVecino: el mejor vecino
    mejorLongitudDeRuta: la mejor longitud de ruta
    
"""
def ascensionColina(tsp):
    solucionActual = solucionAleatoria(tsp)
    actualLongitudDeRuta = longRuta(tsp, solucionActual)
    vecinos = obtenerVecinos(solucionActual)
    mejorVecino, mejorVecinoRouteLength = obtenerMejorVecino(tsp, vecinos)

    while mejorVecinoRouteLength < actualLongitudDeRuta:
        solucionActual = mejorVecino
        actualLongitudDeRuta = mejorVecinoRouteLength
        vecinos = obtenerVecinos(solucionActual)
        mejorVecino, mejorVecinoRouteLength = obtenerMejorVecino(tsp, vecinos)

    return solucionActual, actualLongitudDeRuta

def main():
    # travel salesman problem
    tsp = [
        [0, 400, 500, 300],
        [400, 0, 300, 500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]

    print(ascensionColina(tsp))

if __name__ == "__main__":
    main()