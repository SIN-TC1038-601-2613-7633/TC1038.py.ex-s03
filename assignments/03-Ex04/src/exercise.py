def main():
    """
    Escribe un algoritmo que verifique si una persona puede obtener su licencia de conducir. Para hacerlo debe ser mayor de edad (18 años o más) y traer una identificación oficial. 
    """
    #escribe tu código abajo de esta línea

    edad = int(input("Edad:"))
    licencia = input("¿Tiene licencia (si/no)?")

    if edad >= 18 and licencia == "si":
        print("Puede obtener su licencia de conducir")
    else:
        print("No puede obtener su licencia de conducir")

if __name__=='__main__':
    main()
