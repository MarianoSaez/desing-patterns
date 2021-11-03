from Database import Database


class Oracle(Database):
    def __init__(self, ip : str = "localhost", port : int = 1512) -> None:
        super().__init__(ip, port)

    def connect(self) -> None:
        print("Conectandose a Oracle...")

    def disconnect(self) -> None:
        print("Desconectandose a Oracle...")

    def query1(self) -> list:
        print("Consultando a Oracle...")
        return [{
            "id" : i,
            "nombre" : f"nombre{i}",
        } for i in range(10)]
