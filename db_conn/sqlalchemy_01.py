import sqlalchemy as sa
from sqlalchemy.engine import reflection
import credentials

# Connection parameters
database_name = credentials.database_name
username = credentials.username
password = credentials.password
host = credentials.host
port = credentials.port

# Create an SQLAlchemy engine
engine = sa.create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database_name}")

# Use SQLAlchemy's reflection to get information about the database schema
inspector = reflection.Inspector.from_engine(engine)

# Get the list of all tables
table_names = inspector.get_table_names()

# Print all table names
print("Tables in the 'beautiful_garden' database:")
for table_name in table_names:
    print(table_name)

# No need to close the engine, SQLAlchemy handles connection pooling
