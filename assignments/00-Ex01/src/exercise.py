def main():
    """
    Escribe un algoritmo para verificar si un precio dado por el usuario es válido o no lo es, para ser válido debe ser un valor positivo.
    """
    #escribe tu código abajo de esta línea

    precio = float(input("Dame el precio de un articulo:"))
    
    if precio > 0:
        print("Precio válido")
    else:
        print("Precio inválido")

if __name__=='__main__':
    main()
