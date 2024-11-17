import os
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Float, String, MetaData, Table, ForeignKey, text

script_dir = os.path.dirname(os.path.abspath(__file__))

# Load data from CSV files
stations_df = pd.read_csv(os.path.join(script_dir, 'clean_stations.csv'))
measure_df = pd.read_csv(os.path.join(script_dir, 'clean_measure.csv'))

# Create a SQLite database engine
engine = create_engine(f'sqlite:///{os.path.join(script_dir, "weather_data.db")}', echo=True)
meta = MetaData()

# Define the 'stations' table
stations = Table(
    'stations', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float)
)

# Define the 'measure' table
measure = Table(
    'measure', meta,
    Column('id', Integer, primary_key=True),
    Column('station', Integer, ForeignKey('stations.id')),  # Foreign key to 'stations' table
    Column('date', String),
    Column('precip', Float),
    Column('tobs', Float)
)

# Create tables in the database
meta.create_all(engine)

# Save DataFrame data to the 'stations' table
df_stations_to_db = stations_df.to_sql('stations', con=engine, if_exists='replace', index=False)

# Save DataFrame data to the 'measure' table
df_measure_to_db = measure_df.to_sql('measure', con=engine, if_exists='replace', index=False)

# Connect to the database and execute a sample query

# Define the query
query = text('''
    SELECT * FROM stations LIMIT 5
''')

# Execute the query
with engine.connect() as conn:
    result = conn.execute(query).fetchall()

# Print the result
for row in result:
    print(row)