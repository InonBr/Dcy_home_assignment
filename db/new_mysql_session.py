from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()

host = os.getenv("SQL_HOST")
db_user = os.getenv("DB_USER")
password = os.getenv("PASSWORD")
db_name = os.getenv("DATABASE")

# mysql_connection_string = f"mysql+pymysql://{db_user}:{password}@{host}/{db_name}"
mysql_connection_string = f"mysql+pymysql://{db_user}:{password}@{host}/{db_name}"

engine = create_engine(mysql_connection_string)
Session = sessionmaker(bind=engine)
session = Session()
