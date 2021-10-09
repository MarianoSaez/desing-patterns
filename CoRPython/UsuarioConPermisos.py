from BaseHandler import BaseHandler


# Manejador concreto - UsuarioConPermisos
class UsuarioConPermisos(BaseHandler):
    def __init__(self):
        super().__init__()
     
    def handle(self, request):
        usuarios_con_permisos = ["esteban", "juan", "baltazar", "tira"]
        if request in usuarios_con_permisos:
            print(f"""
            Help:
                Como [USUARIO CON PERMISOS] las opciones son las siguientes:
                comando [-r, --read] [-a, --append] [-c, --change]
            """)
        else:
            type(self).siguiente.handle(request)