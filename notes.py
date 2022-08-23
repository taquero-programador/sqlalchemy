# sqlalchemy
# python3 -m ven ven
# pip install sqlalchemy
# comprobar la versión
import sqlalchemy
sqlalchemy.__version__
# debe corresponder a la 1.4.40

# azul derecha CORE
# azul izquiera ORM

"""
establecer conectividad - engine.
el inicio de cualquier app sqlalchemy es un objeto llamado engine().
actua como una fuente central de conectividad.

se configura usando cadena URL que describa como conectarse a la host o backend.
"""
# usar sqlite
from sqlalchemy import create_engine
sql_url = "sqlite+pysqlite:///./app.db"
engine = create_engine(sql_url, echo=True, future=True)
# echo permite llevar un registro de SQL y lo escribe en la salida estandar


