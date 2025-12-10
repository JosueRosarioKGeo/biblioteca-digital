# Sistema de Búsqueda y Reportes 
from libros import libros 
from prestamos import prestamos 
 
def buscar_por_titulo(termino): 
    """Busca libros por título""" 
    if not termino: 
        print("Error: Debe ingresar un término de búsqueda") 
        return [] 
     
    resultados = [libro for libro in libros.values()  
                  if termino.lower() in libro['titulo'].lower()] 
     
    if not resultados: 
        print("No se encontraron resultados") 
        return [] 
     
    print(f"\n=== Encontrados {len(resultados)} resultados ===") 
    for libro in resultados: 
        print(f"{libro['titulo']} - {libro['autor']}") 
    return resultados


def buscar_por_autor(autor): 
    """Busca libros por autor""" 
    resultados = [libro for libro in libros.values()  
                  if autor.lower() in libro['autor'].lower()] 
    return resultados 
 
def buscar_por_categoria(categoria): 
    """Busca libros por categoría""" 
    resultados = [libro for libro in libros.values()  
                  if libro['categoria'].lower() == categoria.lower()] 
    return resultados 


def libros_disponibles(): 
    """Lista solo los libros disponibles""" 
    disponibles = [libro for libro in libros.values() if libro['disponible']] 
     
    print(f"\n=== LIBROS DISPONIBLES ({len(disponibles)}) ===") 
    for libro in disponibles: 
        print(f"{libro['titulo']} - {libro['autor']}") 
     
    return disponibles

