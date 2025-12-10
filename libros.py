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
