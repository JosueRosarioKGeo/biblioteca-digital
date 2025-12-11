# Sistema Principal de Biblioteca Digital
from config import *
from usuarios import *
from libros import *
from prestamos import *
from busqueda import *
def main():
 print(f"Bienvenido al {NOMBRE_SISTEMA} v{VERSION}")

 # Datos de prueba
 agregar_libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", "Ficción")
 agregar_libro("Don Quijote", "Miguel de Cervantes", "978-8424934644", "Clásicos")
 registrar_usuario("Ana García", "ana@email.com", "809-555-0001")
 registrar_usuario("Carlos López", "carlos@email.com", "809-555-0002")

 listar_libros()
 listar_usuarios()
 realizar_prestamo(1, 1)
 listar_prestamos_activos()
 generar_reporte_general()
if __name__ == "__main__":
 main()