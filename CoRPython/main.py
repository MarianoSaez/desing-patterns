"""
Se simula el comportamiento en el que un usuario que ingresa
el flag --help para un programa de consola y segun el grupo
al que pertenezca el usuario, el output del comando mostrara
mas o menos opciones. Los diferentes manejadores concretos:
    - SuperUsuario
    - UsuarioConPermisos
    - UsuarioBase
    - Invitados
Son los encargados de mostrar los diferentes outputs para los
diferentes usuarios.
"""
from Cliente import Cliente


if __name__ == "__main__":
    cliente = Cliente()
    cliente.handle("baltazar")
