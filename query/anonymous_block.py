from Configuration.oracle_conection import OracleConnection

def example_1():
    sql_results = []
    ora_conn = OracleConnection()
    ora_conn.connect()
    ora_conn.open_cursor()
    ora_conn.cursor.callproc("dbms_output.enable")
    ora_conn.execute_cursor('''DECLARE

    TEST NUMBER;

    BEGIN
        FOR DATA IN (
            SELECT Field_1, Field_2
              FROM Table_1
             WHERE 1=1        
            )LOOP
              DBMS_OUTPUT.PUT_LINE (DATA.Field_1 || DATA.Field_2) ;
        END LOOP;
    END; 

''')
    # perform loop to fetch the text that was added by PL/SQL
    textVar = ora_conn.cursor.var(str)
    statusVar = ora_conn.cursor.var(int)
    sql_return = ''
    while True:
        ora_conn.cursor.callproc("dbms_output.get_line", (textVar, statusVar))
        if statusVar.getvalue() != 0:
            break
        sql_return += textVar.getvalue()
        return (sql_return)