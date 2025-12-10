# Sistema de Gestión de Libros 
libros = {} 
id_contador = 1 
 
def agregar_libro(titulo, autor, isbn, categoria): 
    """Agrega un nuevo libro a la biblioteca""" 
    global id_contador 
     
    if not titulo or not autor or not isbn: 
        print("Error: Todos los campos son obligatorios") 
        return False 
     
    if isbn in [libro['isbn'] for libro in libros.values()]: 
        print("Error: El ISBN ya existe") 
        return False 
     
    libros[id_contador] = { 
        'titulo': titulo, 
        'autor': autor, 
        'isbn': isbn, 
        'categoria': categoria, 
        'disponible': True 
    } 
    print(f"Libro '{titulo}' agregado con ID: {id_contador}") 
    id_contador += 1 
    return True


def listar_libros(): 
    """Lista todos los libros registrados""" 
    if not libros: 
        print("No hay libros registrados") 
        return 
     
    print("\n=== CATÁLOGO DE LIBROS ===") 
    for id_libro, datos in libros.items(): 
        estado = "Disponible" if datos['disponible'] else "Prestado" 
        print(f"ID: {id_libro} | {datos['titulo']} - {datos['autor']} [{estado}]") 
 
def obtener_libro(id_libro): 
    """Obtiene información de un libro por ID""" 
    return libros.get(id_libro) 
 
def actualizar_disponibilidad(id_libro, disponible): 
    """Actualiza el estado de disponibilidad de un libro""" 
    if id_libro in libros: 
        libros[id_libro]['disponible'] = disponible 
        return True 
    return False 