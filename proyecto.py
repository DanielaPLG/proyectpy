#Función del menu
def mostrar_menu():
    print("\n===== ORGANIZADOR DE BIBLIOTECA =====")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Ver todos los libros")
    print("4. Salir")

#Función para agregar libros a tu biblioteca
def agregar_libro(biblioteca):
    titulo = input("Ingresa el título del libro: ").strip()
    autor = input("Ingresa el autor del libro: ").strip()
    biblioteca.append({"titulo": titulo, "autor": autor})
    print("✅Libro agregado correctamente.")

#Función para buscar libro 
def buscar_libro(biblioteca): 
    criterio = input("Buscar por título o autor: ").strip().lower()
    
    print("\n🔎Buscando en la biblioteca...")
    print("Lista de libros disponibles:")
    for libro in biblioteca:
        print(f"- {libro['titulo']} ({libro['autor']})")  
    
    resultados = [libro for libro in biblioteca if criterio in libro["titulo"].lower() or criterio in libro["autor"].lower()]
    
    if resultados:
        print("\n Libros encontrados:")
        for libro in resultados:
            print(f"- 📖{libro['titulo']} ({libro['autor']})")
    else:
        print("❌ No se encontró ningún libro.")

def ver_libros(biblioteca):
    if biblioteca:
        print("\n📚  Lista de libros disponibles:")
        for i, libro in enumerate(biblioteca, start=1):
            print(f"{i}.📖 {libro['titulo']} ({libro['autor']})")
    else:
        print("❌ No hay libros en la biblioteca.")

#Lista de los libros en biblioteca
def main():
    # Lista de libros
    biblioteca = [
        {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
        {"titulo": "1984", "autor": "George Orwell"},
        {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
        {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry"},
        {"titulo": "Harry Potter y la piedra filosofal", "autor": "J.K. Rowling"},
    ]

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            agregar_libro(biblioteca)
        elif opcion == "2":
            buscar_libro(biblioteca)
        elif opcion == "3":
            ver_libros(biblioteca)
        elif opcion == "4":
            print("🏃‍♂️Saliendo. ¡Nos vemos luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
