from mcp_server.db import Database
from mcp_server.security import QuerySecurity


class MCPTools:
    def __init__(self):
        self.db = Database()

    def list_tables(self):
        query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
        """
        return self.db.execute_select(query)

    def describe_table(self, table_name: str):
        query = """
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = %s;
        """
        return self.db.execute_select(query, (table_name,))

    def run_safe_query(self, query: str):
        QuerySecurity.validate_query(query)
        return self.db.execute_select(query)
