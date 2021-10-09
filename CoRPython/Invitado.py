from BaseHandler import BaseHandler


# Manejador concreto - Invitado
class Invitado(BaseHandler):
    def __init__(self):
        super().__init__()

    def handle(self, request):
        # Si no cumplio el resto de permisos se lo
        # supone como invitado
        print(f"""
        Help:
            Como [INVITADO] las opciones son las siguientes:
            comando [-r, --read]
        """)
