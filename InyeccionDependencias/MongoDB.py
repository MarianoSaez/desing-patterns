from Database import Database


class MongoDB(Database):
    def __init__(self, ip : str = "localhost", port : int = 27017) -> None:
        super().__init__(ip, port)

    def connect(self) -> None:
        print("Conectandose a MongoDB...")

    def disconnect(self) -> None:
        print("Desconectandose a MongoDB...")

    def query1(self) -> list:
        print("Consultando a MongoDB...")
        return [{
            "id" : i,
            "nombre" : f"nombre{i}",
        } for i in range(10)]
