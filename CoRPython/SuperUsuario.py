from BaseHandler import BaseHandler


# Manejador concreto - SuperUsuario
class SuperUsuario(BaseHandler):
    def __init__(self):
        super().__init__()
     
    def handle(self, request):
        super_usuarios = ["mariano", "agustin", "bruno", "matias"]
        if request in super_usuarios:
            print(f"""
            Help:
                Como [SUPER USUARIO] las opciones son las siguientes:
                comando [-r, --read] [-a, --append] [-c, --change] [-D, --deleteAll]
            """)
        else:
            type(self).siguiente.handle(request)
