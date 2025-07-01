import sqlite3
import pandas as pd
import logging
import os

# --- Logging setup ---
logging.basicConfig(
    level=logging.INFO,
    filename='test.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('test')
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# --- Connect to SQLite ---
def connect_sqlite(db_file):
    conn = sqlite3.connect(db_file)
    logger.info(f"Connected to SQLite database: {db_file}")
    return conn

# --- Create table ---
def create_table(conn, table_name, columns: dict):
    cursor = conn.cursor()
    column_defs = ", ".join([f'"{col}" {dtype}' for col, dtype in columns.items()])
    query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({column_defs})'
    logger.info(f"Creating table '{table_name}' with columns: {list(columns.keys())}")
    with conn:
        cursor.execute(query)
    logger.info(f"Table '{table_name}' created or already exists")

# --- Insert DataFrame into table ---
def insert_dataframe(conn, df, table_name):
    cols = ", ".join([f'"{col}"' for col in df.columns])
    placeholders = ", ".join(["?"] * len(df.columns))
    insert_sql = f'INSERT INTO "{table_name}" ({cols}) VALUES ({placeholders})'
    values = [tuple(row) for row in df.values]
    with conn:
        conn.executemany(insert_sql, values)
    logger.info(f"Inserted {len(df)} rows into table '{table_name}'")

# --- Read from table ---
def read_table(conn, table_name):
    query = f'SELECT * FROM "{table_name}"'
    df = pd.read_sql(query, conn)
    logger.info(f"Retrieved {len(df)} rows from table '{table_name}'")
    return df

# --- Delete table if it exists ---
def delete_table(conn, table_name):
    query = f'DROP TABLE IF EXISTS "{table_name}"'
    with conn:
        conn.execute(query)
    logger.info(f"Deleted table '{table_name}' if it existed") 

# --- Main function ---
def main():
    db_file = "test_class.db"
    csv_file = "extracted_data.csv"
    table_name = "invoice"

    if not os.path.isfile(csv_file):
        logger.error(f"CSV file '{csv_file}' not found.")
        return

    conn = connect_sqlite(db_file)

    # Read CSV safely (handles BOM)
    df = pd.read_csv(csv_file, encoding="utf-8-sig")

    # Sanitize column names (handle numbers and spaces)
    df.columns = [
        f"col_{col.strip()}" if str(col).strip().isdigit()
        else str(col).strip().replace(" ", "_").replace("-", "_")
        for col in df.columns
    ]
    logger.info(f"Sanitized column names: {df.columns.tolist()}")

    # Define column types for table creation
    columns = {col: 'TEXT' for col in df.columns}

    # ✅ Drop table if it exists (important to avoid schema mismatch)
    delete_table(conn, table_name)

    # Create, insert, and read back data
    create_table(conn, table_name, columns)
    insert_dataframe(conn, df, table_name)
    retrieved_df = read_table(conn, table_name)

    logger.info(f"Data retrieved from table '{table_name}':\n{retrieved_df.head()}")
    
    conn.close()
    logger.info("Connection closed.")

# --- Entry point ---
if __name__ == "__main__":
    main()
