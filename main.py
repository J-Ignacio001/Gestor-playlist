def menu():
    print("\n==============================")
    print("\t.-:Menu:-.")
    print("==============================")
    print("1.- Agregar cancion")
    print("2.- Ver canciones disponibles")
    print("3.- Eliminar una cancion")
    print("4.- Buscar canciones")
    print("5.- Salir del programa \n")

nombres = []
autores = []

def agregar_cancion ():
    nombre = input("Ingrese el nombre de la cancion: ")
    autor = input("Ingrese el autor de la cancion: ")

    nombres.append(nombre)
    autores.append(autor)

    print("\nCancion agregada exitosamente!")
    print(f"{nombre} - {autor}")

def ver_cancion ():
    if len(nombres) == 0:
        print("\nNo hay canciones registradas anteriormente.")
    else:
        print("\n--- Lista de canciones ---")
        for i in range(len(nombres)):
            print(f"{i + 1}. {nombres[i]} - {autores[i]}")

def buscar_cancion ():
    search = input("Ingresa el nombre de la cancion: ")
    encontrado = False
        
    for i in range(len(nombres)):
        if nombres[i].lower() == search.lower():
            print("\n--- Cancion encontrada! ---")
            print(f"{nombres[i]} - {autores[i]}")
            encontrado = True
    if encontrado == False:
        print("\nNo hay canciones registradas anteriormente.")

    
def eliminar ():
    search = input("Ingresa el nombre de la cancion a eliminar: ")
    encontrado = False

    for i in range(len(nombres)):
        if nombres[i].lower() == search.lower():
            print("\n--- Cancion Eliminada ---")
            print(f"{nombres[i]} - {autores[i]}")

            nombres.pop(i)
            autores.pop(i)
            encontrado = True
            break

    if encontrado == False:
        print("\nCancion inexistente. Intente de nuevo.")
                
