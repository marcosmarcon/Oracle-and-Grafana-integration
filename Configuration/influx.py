from influxdb import InfluxDBClient

class InfluxConnection:
    points = []

    def __init__(self):
        self.points = []
        self.host = "host"
        self.port = "port"
        self.username = "user"
        self.password = "pass"
        self.database = "base"

        self.client = InfluxDBClient(self.host, self.port, self.username, self.password, self.database)

    def drop_current_measurement(self, measurement):
        self.client.query("DROP MEASUREMENT """ + measurement + """""")

    def append_point(self, point):
        self.points.append(point)

    def write_points(self):
        self.client.write_points(self.points)

    def clean_points(self):
        self.points = []