from Database import Database
from MySQL import MySQL
from Oracle import Oracle
from MongoDB import MongoDB


class App:
    def __init__(self, db : Database) -> None:
        self.db = db


if __name__ == "__main__":
    db = Oracle("localhost", 1512)
    app = App(db)
    
    app.db.connect()
    result = app.db.query1()
    print(result)
    app.db.disconnect()
