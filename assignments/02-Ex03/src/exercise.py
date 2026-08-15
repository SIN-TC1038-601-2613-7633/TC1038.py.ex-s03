def main():
    """
    Escribe un algoritmo que dada una longitud en metros, calcule y muestre su equivalente en pies.
    Recuerda que 1 pie = 12 pulgadas, 1 pulgada = 2.54 cm, 1 m = 100 cm
    """

    #escribe tu código abajo de esta línea

    longitud_m = float(input("Longitud en metros:"))

    longitud_cms = longitud_m * 100
    longitud_plg = longitud_cms / 2.54
    longitud_pie = longitud_plg / 12

    print("Longitud en pies:", longitud_pie) 

if __name__=='__main__':
    main()
