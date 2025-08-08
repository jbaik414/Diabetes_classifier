import os
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd

load_dotenv()


def get_connection():
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )
    return conn


def load_data():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM SUPPLY_CHAIN_FOR_DASHBOARD")
        df = cur.fetch_pandas_all()
        df.columns = [col.upper() for col in df.columns]
        return df
    finally:
        cur.close()
        conn.close()
