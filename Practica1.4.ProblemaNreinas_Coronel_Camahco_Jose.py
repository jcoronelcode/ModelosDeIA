import random
import time

start = time.time()  # Registro del tiempo de inicio para medir la duración del algoritmo

# Definición de parámetros para el algoritmo genético
nPersonas = 4  # Tamaño de la población (número de cromosomas)
n = 10  # Número de reinas y tamaño del tablero
LIMITE = 20  # Umbral mínimo de fitness para seleccionar cromosomas

# Inicialización de variables y estructuras de datos
poblacion = []*nPersonas  # Lista para almacenar la población de cromosomas
nuevaPoblacion = []  # Lista para la nueva población tras selección y mutación
fx = [0]*nPersonas  # Lista para el valor de fitness de cada cromosoma
fxPorciento = [0]*nPersonas  # Lista para el porcentaje de fitness de cada cromosoma
encontrado = -1  # Variable para indicar si se ha encontrado una solución

# Función para calcular el número de amenazas en un cromosoma (solución propuesta)
def amenazadas(cromosoma):
    nAmenazas = 0
    # Comparación de cada reina con las demás para contar las amenazas
    for i in range(n-1):
        for x in range(i+1, n):
            # Comprueba si hay otra reina en la misma columna o diagonal
            if cromosoma[i] == cromosoma[x] or abs(cromosoma[x]-cromosoma[i]) == abs(x-i):
                nAmenazas += 1  # Incrementa el contador de amenazas
    return nAmenazas

# Función para calcular el fitness de cada individuo y verificar si hay una solución
def fitnes(po, nCro, nPer):
    totalAmenazas = 0
    # Calcula el número máximo de amenazas posibles para una solución incorrecta
    for i in range(nCro):
        totalAmenazas += nCro-1-i
    nReinasNoAtacan = 0
    encontrado = -1
    # Calcula el fitness para cada cromosoma en la población
    for i in range(nPer):
        fx[i] = totalAmenazas - amenazadas(po[i])  # Fitness basado en amenazas reducidas
        nReinasNoAtacan += fx[i]  # Suma de fitness total
        if fx[i] == totalAmenazas:  # Verifica si el cromosoma es una solución perfecta
            encontrado = i
    print('Número de pares de cromosomas que no se amenazan:\n', fx)
    # Calcula el porcentaje de fitness de cada individuo
    for i in range(nPer):
        fxPorciento[i] = (fx[i]/nReinasNoAtacan) * 100
    print("Fuerza de los cromosomas:\n", fxPorciento)
    return encontrado  # Devuelve el índice del cromosoma solución si lo encuentra

# Generación inicial de la población aleatoria
for i in range(nPersonas):
    cromosoma = []
    for x in range(n):
        cromosoma.append(random.randint(0, n-1))  # Asigna una posición aleatoria para cada reina
    poblacion.append(cromosoma)
print("Población inicial: \n", poblacion)

# Bucle principal de búsqueda hasta encontrar una solución
while encontrado == -1:
    # Cálculo del fitness para cada individuo en la población
    encontrado = fitnes(poblacion, n, nPersonas)
    if encontrado == -1:  # Si no se ha encontrado solución, procede con selección y mutación
        nuevaPoblacion = []
        # Selección de los cromosomas con fitness superior al límite
        for i in range(nPersonas):
            if fxPorciento[i] > LIMITE:
                nuevaPoblacion.append(poblacion[i])
        # Completa la población si no es suficiente seleccionando aleatoriamente de la mejor población
        if nuevaPoblacion:
            for i in range(len(nuevaPoblacion), nPersonas):
                cromoAux = random.choice(nuevaPoblacion)  # Selección aleatoria de la mejor población
                cromoAux2 = cromoAux.copy()  # Copia el cromosoma seleccionado
                nuevaPoblacion.append(cromoAux2)
        else:
            nuevaPoblacion = poblacion  # Si no hay individuos con fitness suficiente, usa la misma población
        print('Grupo de cromosomas que tuvieron mejor fitness:\n', nuevaPoblacion)
        
        # Cruce de cromosomas seleccionando puntos de corte aleatorios
        pares = int(nPersonas / 2)
        partes = []
        for i in range(pares):
            partir = random.randint(1, n - 2)  # Punto de corte aleatorio
            partes.append(partir)
            x, y = i * 2, i * 2 + 1
            # Intercambio de genes entre pares de cromosomas a partir del punto de corte
            for z in range(partir, n):
                nuevaPoblacion[x][z], nuevaPoblacion[y][z] = nuevaPoblacion[y][z], nuevaPoblacion[x][z]
        print('Aleatoriamente se ha definido el corte de cada cromosoma a combinar:\n', partes, '\n', nuevaPoblacion)

        # Mutación aleatoria: se cambia un elemento aleatorio de cada cromosoma
        mutados = []
        for i in range(nPersonas):
            aleatorio = random.randint(0, n - 1)
            nuevaPoblacion[i][aleatorio] = random.randint(0, n - 1)
            mutados.append(aleatorio)
        print('Se muta de forma aleatoria un elemento de cada cromosoma de la nueva población:\n', mutados, '\n', nuevaPoblacion)

        # Actualización de la población con la nueva generación
        poblacion = nuevaPoblacion

    else:
        print('Cromosoma encontrado: ', poblacion[encontrado])

end = time.time()
print("Tiempo de ejecución: ", end - start)
