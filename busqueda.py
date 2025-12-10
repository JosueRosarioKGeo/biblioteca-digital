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
