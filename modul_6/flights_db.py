import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def execute_sql(conn, sql):
    """ Execute sql :param conn: Connection object :param sql: a SQL script """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def insert_flights_data(conn):
    """ Insert flight data into the flights table """
    data = [
        ('LO269', '2024-08-02 18:17', '2024-08-02 20:14', 'WAW', 'AMS', 'E75'),
        ('LO270', '2024-08-03 05:14', '2024-08-03 07:16', 'AMS', 'WAW', 'E75'),
        ('LO233', '2024-08-04 14:40', '2024-08-04 16:49', 'WAW', 'BRU', 'E90'),
        ('LO234', '2024-08-04 17:30', '2024-08-04 19:21', 'BRU', 'WAW', 'E90'),
        ('LO791', '2024-08-04 20:55', '2024-08-04 22:29', 'WAW', 'TLL', 'E75'),
        ('LO786', '2024-08-05 12:12', '2024-08-05 13:48', 'TLL', 'WAW', 'E95'),
        ('LO521', '2024-08-05 14:50', '2024-08-05 15:51', 'WAW', 'PRG', 'E95'),
        ('LO528', '2024-08-06 10:44', '2024-08-06 11:53', 'PRG', 'WAW', 'E9A'),
        ('LO537', '2024-08-06 13:32', '2024-08-06 14:51', 'WAW', 'BUD', 'E9A'),
        ('LO538', '2024-08-06 15:34', '2024-08-06 16:44', 'BUD', 'WAW', 'E9A'),
        ('LO3935', '2024-08-06 17:27', '2024-08-06 18:26', 'WAW', 'SZZ', 'E7A'),
        ('LO3936', '2024-08-06 18:53', '2024-08-06 19:49', 'SZZ', 'WAW', 'E7A'),
        ('LO45', '2024-08-09 15:15', '2024-08-10 00:28', 'WAW', 'YYZ', '789'),
        ('LO46', '2024-08-11 02:15', '2024-08-11 10:10', 'YYZ', 'WAW', '789'),
        ('LO355', '2024-08-16 18:40', '2024-08-16 20:20', 'WAW', 'MUC', 'E96'),
        ('LO356', '2024-08-17 05:00', '2024-08-17 06:35', 'MUC', 'WAW', 'E96'),
        ('LO331', '2024-08-18 05:20', '2024-08-18 07:50', 'WAW', 'CDG', 'E9A'),
        ('LO334', '2024-08-19 05:05', '2024-08-19 07:20', 'CDG', 'WAW', 'E9A'),
        ('LO527', '2024-08-19 08:50', '2024-08-19 10:05', 'WAW', 'PRG', 'E7A'),
        ('LO530', '2024-08-20 05:10', '2024-08-20 06:20', 'PRG', 'WAW', 'E75'),
        ('LO387', '2024-08-20 07:15', '2024-08-20 08:30', 'WAW', 'BER', 'E75'),
        ('LO388', '2024-08-20 09:10', '2024-08-20 10:25', 'BER', 'WAW', 'E75'),
        ('LO3805', '2024-08-26 05:15', '2024-08-26 06:05', 'WAW', 'RZE', 'E7A'),
        ('LO3806', '2024-08-26 06:45', '2024-08-26 07:35', 'RZE', 'WAW', 'E7A'),
        ('LO3945', '2024-08-26 08:25', '2024-08-26 09:20', 'WAW', 'POZ', 'E7A'),
        ('LO3942', '2024-08-27 03:40', '2024-08-27 04:35', 'POZ', 'WAW', 'E75'),
        ('LO417', '2024-08-27 05:25', '2024-08-27 07:45', 'WAW', 'GVA', 'E75'),
        ('LO418', '2024-08-27 08:25', '2024-08-27 10:35', 'GVA', 'WAW', 'E75'),
        ('LO571', '2024-08-29 09:35', '2024-08-29 11:15', 'WAW', 'BEG', 'E90'),
        ('LO572', '2024-08-29 11:55', '2024-08-29 13:35', 'BEG', 'WAW', 'E90'),
        ('LO483', '2024-08-29 14:50', '2024-08-29 16:55', 'WAW', 'OSL', 'E96'),
        ('LO484', '2024-08-29 17:45', '2024-08-29 19:40', 'OSL', 'WAW', 'E96')
    ]
    try:
        c = conn.cursor()
        c.executemany("""
            INSERT OR IGNORE INTO flights (flight_number, departure_date_time, arrival_date_time, departure_airport, arrival_airport, aircraft_type)
            VALUES (?, ?, ?, ?, ?, ?)
        """, data)
        conn.commit()
    except Error as e:
        print(e)

def insert_product_standards(conn):
    """ Insert product standards data into the product_standards table """
    data = [
        ('AMS', 'WAW', 'B2'),
        ('FCO', 'RDO', 'B2'),
        ('MAD', 'WAW', 'D'),
        ('SPU', 'WAW', 'B2'),
        ('ARN', 'WAW', 'B2'),
        ('FCO', 'WAW', 'B2'),
        ('MUC', 'WAW', 'B1'),
        ('STR', 'WAW', 'B2'),
        ('ATH', 'WAW', 'B2'),
        ('FRA', 'WAW', 'B2'),
        ('MXP', 'RZE', 'B2'),
        ('SZY', 'KRK', 'A'),
        ('BCN', 'WAW', 'D'),
        ('GDN', 'RZE', 'A'),
        ('MXP', 'WAW', 'B2'),
        ('SZZ', 'WAW', 'A'),
        ('BEG', 'WAW', 'B2'),
        ('GDN', 'WAW', 'A'),
        ('NCE', 'WAW', 'C'),
        ('TAS', 'WAW', 'F'),
        ('BER', 'WAW', 'B1'),
        ('GOT', 'WAW', 'B2'),
        ('NQZ', 'WAW', 'F'),
        ('TBS', 'WAW', 'D'),
        ('BEY', 'WAW', 'E'),
        ('GVA', 'WAW', 'B2'),
        ('OHD', 'RDO', 'B2'),
        ('TGD', 'RDO', 'B2'),
        ('BLL', 'WAW', 'B1'),
        ('GYD', 'WAW', 'E'),
        ('OSL', 'WAW', 'B2'),
        ('TGD', 'WAW', 'B2'),
        ('BRU', 'WAW', 'C'),
        ('HAM', 'WAW', 'B1'),
        ('OSR', 'WAW', 'A'),
        ('TIA', 'RDO', 'B2'),
        ('BUD', 'WAW', 'A'),
        ('IEG', 'WAW', 'A'),
        ('OTP', 'WAW', 'B2'),
        ('TIA', 'WAW', 'B2'),
        ('BZG', 'KRK', 'A'),
        ('IST', 'KRK', 'C'),
        ('POZ', 'WAW', 'A'),
        ('TLL', 'WAW', 'B1'),
        ('BZG', 'WAW', 'A'),
        ('IST', 'WAW', 'C'),
        ('PRG', 'WAW', 'A'),
        ('TLV', 'KRK', 'D'),
        ('CAI', 'WAW', 'E'),
        ('KRK', 'WAW', 'A'),
        ('PVK', 'RDO', 'B2'),
        ('TLV', 'WAW', 'D'),
        ('CDG', 'WAW', 'C'),
        ('KSC', 'WAW', 'A'),
        ('RIX', 'WAW', 'A'),
        ('VCE', 'WAW', 'B2'),
        ('CLJ', 'WAW', 'B2'),
        ('KTW', 'WAW', 'A'),
        ('RMO', 'WAW', 'B2'),
        ('VIE', 'WAW', 'B1'),
        ('CPH', 'WAW', 'B1'),
        ('LCY', 'VNO', 'C'),
        ('RUH', 'WAW', 'F'),
        ('VNO', 'WAW', 'A'),
        ('DBV', 'WAW', 'B2'),
        ('LHR', 'WAW', 'C'),
        ('RZE', 'WAW', 'A'),
        ('WRO', 'WAW', 'A'),
        ('DUS', 'WAW', 'B2'),
        ('LJU', 'WAW', 'B2'),
        ('SJJ', 'WAW', 'B2'),
        ('ZAG', 'WAW', 'B2'),
        ('DXB', 'WAW', 'F'),
        ('LUX', 'WAW', 'B2'),
        ('SKP', 'WAW', 'B2'),
        ('ZRH', 'WAW', 'B2'),
        ('EVN', 'WAW', 'D'),
        ('LUZ', 'WAW', 'A'),
        ('SOF', 'WAW', 'B2')
    ]

    reverse_data = [(arrival, departure, standard) for (departure, arrival, standard) in data]
    data.extend(reverse_data)

    try:
        c = conn.cursor()
        c.executemany("""
            INSERT OR IGNORE INTO product_standards (departure_airport, arrival_airport, standard)
            VALUES (?, ?, ?)
        """, data)
        conn.commit()
    except Error as e:
        print(e)

def select_all(conn, table):
   """
   Query all rows in the table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()

   return rows

def select_where(conn, table, **query):
   """
   Query tasks from table with data from **query dict
   :param conn: the Connection object
   :param table: table name
   :param query: dict of attributes and values
   :return:
   """
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows

def update_aircraft_type(conn, flight_id, new_aircraft_type):
    """
    Update the aircraft type of a flight
    :param conn: the Connection object
    :param flight_id: id of the flight to update
    :param new_aircraft_type: new aircraft type
    :return:
    """
    sql = ''' UPDATE flights
              SET aircraft_type = ?
              WHERE id = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, (new_aircraft_type, flight_id))
        conn.commit()
        print("Aircraft type updated successfully")
    except sqlite3.OperationalError as e:
        print(e)

def delete_where(conn, table, **kwargs):
   """
   Delete from table where attributes from
   :param conn:  Connection to the SQLite database
   :param table: table name
   :param kwargs: dict of attributes and values
   :return:
   """
   qs = []
   values = tuple()
   for k, v in kwargs.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)

   sql = f'DELETE FROM {table} WHERE {q}'
   cur = conn.cursor()
   cur.execute(sql, values)
   conn.commit()
   print("Deleted")

def delete_all(conn, table):
   """
   Delete all rows from table
   :param conn: Connection to the SQLite database
   :param table: table name
   :return:
   """
   sql = f'DELETE FROM {table}'
   cur = conn.cursor()
   cur.execute(sql)
   conn.commit()
   print("Deleted")

if __name__ == "__main__":
    # SQL to create flights table
    create_flights_table_sql = """
    CREATE TABLE IF NOT EXISTS flights (
        id INTEGER PRIMARY KEY,
        flight_number VARCHAR(6) NOT NULL,
        departure_date_time TEXT NOT NULL,
        arrival_date_time TEXT NOT NULL,
        departure_airport VARCHAR(3) NOT NULL,
        arrival_airport VARCHAR(3) NOT NULL,
        aircraft_type VARCHAR(3) NOT NULL,
        FOREIGN KEY (departure_airport, arrival_airport) REFERENCES product_standards (departure_airport, arrival_airport),
        UNIQUE(flight_number, departure_date_time)
    );
    """

    # SQL to create product_standards table
    create_product_standards_table_sql = """
    CREATE TABLE IF NOT EXISTS product_standards (
        id INTEGER PRIMARY KEY,
        departure_airport VARCHAR(3) NOT NULL,
        arrival_airport VARCHAR(3) NOT NULL,
        standard VARCHAR(20) NOT NULL,
        UNIQUE(departure_airport, arrival_airport)
    );
    """

    # Create a database connection
    db_file = "flights_database.db"
    with create_connection(db_file) as conn:
        if conn is not None:
            execute_sql(conn, create_product_standards_table_sql)
            execute_sql(conn, create_flights_table_sql)
            # CREATE
            insert_product_standards(conn)
            insert_flights_data(conn)
            # READ
            print("Initial flights data:")
            flights = select_all(conn, "flights")
            for flight in flights:
                print(flight)
            sequencesE = select_where(conn, "product_standards", standard="E")
            for sequence in sequencesE:
                print(sequence)
            # UPDATE
            print("Updating aircraft type for flight id 1...")
            update_aircraft_type(conn, 1, "E90")
            # DELETE
            print("Deleting flight with id 32...")
            delete_where(conn, "flights", id=32)
            print("After deletion:")
            flights = select_all(conn, "flights")
            for flight in flights:
                print(flight)
            print("Deleting all product standards...")
            delete_all(conn, "product_standards")
        else:
            print("Error! Cannot create the database connection.")