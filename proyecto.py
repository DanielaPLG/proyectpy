def mostrar_menu():
    print("\n===== ORGANIZADOR DE BIBLIOTECA =====")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Ver todos los libros")
    print("4. Salir")

def agregar_libro(biblioteca):
    titulo = input("Ingresa el título del libro: ")
    autor = input("Ingresa el autor del libro: ")
    biblioteca.append({"titulo": titulo, "autor": autor})
    print("Libro agregado correctamente.")

def buscar_libro(biblioteca):
    criterio = input("Buscar por título o autor: ").lower()
    resultados = [libro for libro in biblioteca if criterio in libro["titulo"].lower() or criterio in libro["autor"].lower()]
    if resultados:
        for libro in resultados:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}")
    else:
        print("No se encontró ningún libro.")

def ver_libros(biblioteca):
    if biblioteca:
        print("\nLista de libros disponibles:")
        for libro in biblioteca:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}")
    else:
        print("No se encuentran libros en la biblioteca.")

def main():
    biblioteca = []
    while True:  
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-4): ")
        if opcion == "1":
            agregar_libro(biblioteca)
        elif opcion == "2":
            buscar_libro(biblioteca)
        elif opcion == "3":
            ver_libros(biblioteca)
        elif opcion == "4":
            print("Saliendo.¡Nos vemos luego!")
            break
        else:
            print("Opción no válida, intentalo de nuevo.")

if __name__ == "__main__":
    main()
