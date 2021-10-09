from BaseHandler import BaseHandler


# Manejador concreto - UsuarioBase
class UsuarioBase(BaseHandler):
    def __init__(self):
        super().__init__()
     
    def handle(self, request):
        usuarios_base = ["martin", "tomas", "alfredo", "emanuel"]
        if request in usuarios_base:
            print(f"""
            Help:
                Como [USUARIO BASE] las opciones son las siguientes:
                comando [-r, --read] [-a, --append]
            """)
        else:
            type(self).siguiente.handle(request)