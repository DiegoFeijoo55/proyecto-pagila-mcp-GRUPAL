from .db import get_connection
from .security import validate_query


def list_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """)
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]


def describe_table(table_name: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = '{table_name}'
    """)
    rows = cur.fetchall()
    conn.close()
    return rows


def run_safe_query(query: str):
    validate_query(query)
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query)

    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    conn.close()

    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))

    return results
