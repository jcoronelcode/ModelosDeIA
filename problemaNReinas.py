import random

# Configuración inicial
n = 8  # Tamaño del tablero y número de reinas

def intentar_solucion():
    # Inicializa los marcadores de ataque
    columna = [False] * n
    diagonal_izquierda = [False] * (2 * n)
    diagonal_derecha = [False] * (2 * n)
    
    # Intentamos colocar las reinas fila por fila
    for y in range(n):
        # Generamos una lista aleatoria de columnas disponibles para esta fila
        columnas_disponibles = [x for x in range(n) if not columna[x] and not diagonal_izquierda[x + y] and not diagonal_derecha[x - y + n - 1]]
        random.shuffle(columnas_disponibles)  # Baraja las columnas disponibles
        
        # Si no hay columnas disponibles, indica que falló esta disposición
        if not columnas_disponibles:
            print(f"Reinicio del tablero en la fila {y}. No hay columnas válidas.")
            return False
        
        # Selecciona una columna aleatoria de las disponibles y coloca la reina
        x = columnas_disponibles[0]
        columna[x] = diagonal_izquierda[x + y] = diagonal_derecha[x - y + n - 1] = True
        print(f"Reina colocada en fila {y}, columna {x}.")
    
    # Si se logran colocar todas las reinas, se ha encontrado una solución
    print("Se ha colocado una reina en cada fila sin conflictos.")
    return True

# Realiza intentos hasta encontrar una solución válida
intentos = 1
while not intentar_solucion():
    print(f"Intento {intentos} fallido. Reiniciando tablero completo.")
    intentos += 1

# Indica que se ha encontrado una solución válida
print("¡Solución encontrada después de", intentos, "intentos!")
