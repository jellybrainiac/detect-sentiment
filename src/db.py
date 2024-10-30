import sqlite3


class DBConnection:
    def __init__(self, config):
        try:
            self.connection = sqlite3.connect(config.dir)
        except Exception as e:
            raise e


class DBAction:
    def __init__(self, connection):
        self.cursor = connection.cursor()
        try:
            self.create_table()
        except:
            pass  # Table already exist

    def create_table(self):
        try:
            self.cursor.execute("CREATE TABLE detectresult(name, class, conf)")
        except Exception as e:
            raise e

    def write(self, name, request: dict):
        try:
            assert isinstance(
                request["conf"], list
            )  # Check if request has confidence score
            assert isinstance(request["cls"], list)  # Check if request has class labels
            assert isinstance(name, str)
            # For the sake of simplicity, convert all of them into to string
            conf_scores = str(request["conf"])
            class_labels = str(request["cls"])

            self.cursor.execute(
                f"""INSERT INTO detectresult(name, class, conf) 
                                VALUES(?, ?, ?)""",
                (name, class_labels, conf_scores),
            )
        except Exception as e:
            raise e

    def read(self, request: str):
        try:
            assert isinstance(request, str)
            self.cursor.execute(f"""SELECT * FROM detectresult WHERE name={request}""")
        except Exception as e:
            raise e
