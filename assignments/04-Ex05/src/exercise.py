def main():
    """
    Escribe un algoritmo que calcule el promedio de tres calificaciones parciales de un curso.
    """
    #escribe tu código abajo de esta línea

    calificacion_parcial_1 = float(input("Dame la calificación del Parcial 1:"))
    calificacion_parcial_2 = float(input("Dame la calificación del Parcial 2:"))
    calificacion_parcial_3 = float(input("Dame la calificación del Parcial 3:"))

    promedio = (calificacion_parcial_1+calificacion_parcial_2+calificacion_parcial_3) / 3

    print("Promedio=", promedio)
        
if __name__=='__main__':
    main()
