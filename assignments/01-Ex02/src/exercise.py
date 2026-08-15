def main():
    """
    Escribe un algoritmo que muestre la velocidad promedio de un automóvil dadas la distancia recorrida en kilómetros y el tiempo que se tardó en recorrer esa distancia dado en horas.
    """
    #escribe tu código abajo de esta línea

    distancia = float(input("Distancia recorrida en kilómetros:"))
    tiempo = float(input("Tiempo en horas:"))

    velocidad = distancia / tiempo

    print("Velocidad=", velocidad, "km/hr")

if __name__=='__main__':
    main()
