import duckdb


def create_connection():
    return duckdb.connect(database=":memory:")


def load_dataframe_to_duckdb(conn, df, table_name="sales"):
    conn.register("df_view", df)
    conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df_view")

def get_schema(df):
    cols = df.columns.tolist()
    return ", ".join(cols)