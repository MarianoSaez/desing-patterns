class IHandler():
    def setNext(self, h): raise NotImplementedError
    def getNext(self, h): raise NotImplementedError
    def handle(self, request): raise NotImplementedError
