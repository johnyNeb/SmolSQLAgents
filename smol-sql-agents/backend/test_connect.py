from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

conn_str = (
    f"oracle+oracledb://"
    f"{os.environ['DB_USER']}:"
    f"{os.environ['DB_PASSWORD']}@"
    f"{os.environ['DB_HOST']}:"
    f"{os.environ['DB_PORT']}/"
    f"?service_name={os.environ['DB_SERVICE']}"
)

print("Connecting...")
engine = create_engine(conn_str)

with engine.connect() as conn:
    print("Connection successful!")