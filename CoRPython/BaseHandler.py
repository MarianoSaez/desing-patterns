from IHandler import IHandler


# Clase abstracta que define el comportamiento
# basico de un manejador. Manejadores concretos
# heredan BaseHandler.
class BaseHandler(IHandler):
    siguiente = None

    def handle(self, request):
        raise NotImplementedError

    def setNext(self, h : IHandler) -> None:
        type(self).siguiente = h

    def getNext(self) -> IHandler:
        return type(self).siguiente
