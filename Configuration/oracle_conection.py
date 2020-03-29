import cx_Oracle

class OracleConnection:

    def connect(self):
        uid = "user id"
        pwd = "password"
        sid = "string connection"

        self.connection = cx_Oracle.connect(uid, pwd, sid)

    def open_cursor(self):
        self.cursor = self.connection.cursor()

    def execute_cursor(self, sql):
        self.cursor.execute(sql)

    def close_cursor(self):
        self.cursor.close()

    def close_connection(self):
        self.connection.close()
