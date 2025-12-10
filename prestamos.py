# Sistema de Gestión de Préstamos 
from datetime import datetime, timedelta 
from config import DIAS_PRESTAMO, MAX_PRESTAMOS

prestamos = [] 
id_prestamo = 1 
 
def realizar_prestamo(id_usuario, id_libro): 
    """Registra un nuevo préstamo""" 
    global id_prestamo 

    prestamos_activos = [p for p in prestamos if p['id_usuario'] == id_usuario and not 
p['devuelto']] 
    if len(prestamos_activos) >= MAX_PRESTAMOS: 
        print(f"Error: El usuario ha alcanzado el límite de {MAX_PRESTAMOS} préstamos") 
        return False 
     
fecha_prestamo = datetime.now()
fecha_devolucion = fecha_prestamo + timedelta(days=DIAS_PRESTAMO)

prestamo = {
    'id': id_prestamo,
    'id_usuario': id_usuario,
    'id_libro': id_libro,
    'fecha_prestamo': fecha_prestamo,
    'fecha_devolucion': fecha_devolucion,
    'devuelto': False
}

prestamos.append(prestamo)

print(f"Préstamo #{id_prestamo} registrado. Devolución: {fecha_devolucion.strftime('%d/%m/%Y')}")

id_prestamo += 1
return True
  
def devolver_libro(id_prestamo): 
    """Registra la devolución de un libro""" 
    for prestamo in prestamos: 
        if prestamo['id'] == id_prestamo and not prestamo['devuelto']: 
            prestamo['devuelto'] = True 
            prestamo['fecha_devolucion_real'] = datetime.now() 
            print(f"Libro devuelto correctamente") 
            return True 
     
    print("Error: Préstamo no encontrado o ya devuelto") 
    return False 