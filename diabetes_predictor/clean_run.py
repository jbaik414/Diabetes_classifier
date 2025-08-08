from config.snowflake_config import get_connection
from clean_data import clean_diabetes_data
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd

def load_raw_data():
    conn = get_connection()
    query = "SELECT * FROM PUBLIC.DIABETES_METRICS"
    df = pd.read_sql(query, conn)

    conn.close()
    return df

def upload_cleaned_data(df_clean):
    conn = get_connection()
   

    success, nchunks, nrows, _ = write_pandas(
    conn, df_clean, table_name="DIABETES_CLEANED", auto_create_table=True ,schema="CURATED", database="DIABETES_DATASET", overwrite=True
)
    conn.close()
    print(f"Uploaded {nrows} cleaned rows to Snowflake.")

if __name__ == "__main__":
    df = load_raw_data()
    df_clean = clean_diabetes_data(df)
    upload_cleaned_data(df_clean)
    df_clean.to_csv("cleaned_diabetes_data.csv", index=False)

