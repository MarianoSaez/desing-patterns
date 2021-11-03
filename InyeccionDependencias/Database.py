class Database:
    def __init__(self, ip : str, port : int) -> None:
        self.ip = ip
        self.port = port

    def connect(self) -> None:
        raise NotImplementedError

    def disconnect(self) -> None:
        raise NotImplementedError

    def query1(self) -> list:
        raise NotImplementedError