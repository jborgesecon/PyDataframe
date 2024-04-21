import pandas as pd
from sqlalchemy import create_engine
import credentials

# Replace these with your actual database credentials
db_name = credentials.database_name
username = credentials.username
password = credentials.password
host = credentials.host
port = credentials.port

# Create the connection string
connection_string = f"postgresql://{username}:{password}@{host}:{port}/{db_name}"

# Create the SQLAlchemy engine
engine = create_engine(connection_string)


# Table name (replace with your actual table name)
table_name = "portal_da_transparencia.viagens_2018"

# SQL query to select the first 10 rows
query = f"select nome_org_sup, count(*) from {table_name} group by nome_org_sup order by count(*) desc;"
# query = f"SELECT COUNT(*) FROM {table_name};"

# Execute the query and load the result into a Pandas DataFrame
df = pd.read_sql(query, engine)

# Display the result
print(df)
