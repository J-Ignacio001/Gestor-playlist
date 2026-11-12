import main

validar = 1

while validar !=0:
    main.menu()
    opcion = int(input("Eliga una opcion (1-5): "))
    if opcion == 1:
        main.agregar_cancion()
    elif opcion == 2:
        main.ver_cancion()
    elif opcion == 3:
        main.eliminar()
    elif opcion == 4:
        main.buscar_cancion()
    elif opcion == 5:
        print("Saliste del programa.")
        validar = 0
    else:
        print("Error, numeros no validos. Vuelva a intentar")
