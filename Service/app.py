from Configuration.influx import InfluxConnection
from Configuration.oracle_conection import OracleConnection
from query.anonymous_block import example_1
from query.query import query

def example_anonymous_block():
    return_example_1 = example_1()
    save_influx_anonymous_block(return_example_1)

def example_query():
    return_example_2 = query()
    save_influx_query(return_example_2)

def save_influx_anonymous_block(return_example_1):
    data_1 = return_example_1[1:9]
    data_2 = return_example_1[9:]
    point = {
        "measurement": "measurement_1",
        "fields": {
            "data_1": data_1,

            "data_2": data_2
        },
    }
    save = InfluxConnection()
    save.append_point(point)
    save.write_points()

def save_influx_query( return_example_2):
    point = {
        "measurement": "measurement_2",
        "fields": {
            "data_1": return_example_2
        },
    }
    save = InfluxConnection()
    save.append_point(point)
    save.write_points()