import pandas as pd
from sqlalchemy import create_engine

# CSV file path
csv_file = "data.csv"

# Read CSV
df = pd.read_csv(csv_file)

# Database connection
user = "root"
password = "root"
host = "localhost"
port = 3307
database = "testdb"

engine = create_engine(f"mariadb+mariadbconnector://{user}:{password}@{host}:{port}/{database}")

# Load data into table
df.to_sql('users', con=engine, if_exists='replace', index=False)

print("Data ingested successfully!")
