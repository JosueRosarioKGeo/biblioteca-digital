usuarios = {}
id_usuario_contador = 1
def registrar_usuario(nombre, email, telefono):
    """Registra un nuevo usuario en el sistema"""
    global id_usuario_contador
    
    if not nombre or not email:
        print("Error: Nombre y email son obligatorios")
        return False
    
    if email in [u['email'] for u in usuarios.values()]:
        print("Error: El email ya está registrado")
        return False
    
    usuarios[id_usuario_contador] = {
        'nombre': nombre,
        'email': email,
        'telefono': telefono,
        'prestamos_historicos': 0,
        'activo': True
    }
    print(f"Usuario '{nombre}' registrado con ID: {id_usuario_contador}")
    id_usuario_contador += 1
    return True

def listar_usuarios():
    """Lista todos los usuarios registrados"""
    if not usuarios:
        print("No hay usuarios registrados")
        return
    
    print("\n=== USUARIOS REGISTRADOS ===")
    
    for id_user, datos in usuarios.items():
        estado = "Activo" if datos['activo'] else "Inactivo"
        print(f"ID: {id_user} | {datos['nombre']} - {datos['email']} [{estado}]")
