from BaseHandler import BaseHandler
from Invitado import Invitado
from UsuarioBase import UsuarioBase
from UsuarioConPermisos import UsuarioConPermisos
from SuperUsuario import SuperUsuario


# Eslabon que comienza la cadena
class Cliente(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self, request):
        super_usuario = SuperUsuario()
        usuario_con_permisos = UsuarioConPermisos()
        usuario_base = UsuarioBase()
        invitado = Invitado()

        self.setNext(super_usuario)
        super_usuario.setNext(usuario_con_permisos)
        usuario_con_permisos.setNext(usuario_base)
        usuario_base.setNext(invitado)

        type(self).siguiente.handle(request)
