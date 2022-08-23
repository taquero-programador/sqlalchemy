#!/usr/bin/env python3

from sqlalchemy import create_engine

sql_url = "sqlite+pysqlite:///./app.db"
engine = create_engine(sql_url, echo=True, future=True)


