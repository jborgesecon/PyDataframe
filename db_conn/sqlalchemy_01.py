import credentials as crd
import sqlalchemy as sa, create_engine
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base
import urllib.parse


u = crd.username
psswd = crd.password
h = crd.host
port = crd.port
db = crd.database_name

# Connection string
conn_str = f'postgresql://{u}:{psswd}@{h}:{port}/{db}'
engine = sa.create_engine(conn_str)

with engine.connect() as connection:
    result = connection.execute('select * from services.quantitativo_controladoria_1 qc limit 10;')
    for row in result:
        print(row)

