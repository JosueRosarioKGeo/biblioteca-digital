# Sistema de Gestión de Usuarios
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
