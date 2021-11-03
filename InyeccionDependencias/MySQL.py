from Database import Database


class MySQL(Database):
    def __init__(self, ip : str = "localhost", port : int = 3306) -> None:
        super().__init__(ip, port)

    def connect(self) -> None:
        print("Conectandose a MySQL...")

    def disconnect(self) -> None:
        print("Desconectandose a MySQL...")

    def query1(self) -> list:
        print("Consultando a MySQL...")
        return [{
            "id" : i,
            "nombre" : f"nombre{i}",
        } for i in range(10)]
