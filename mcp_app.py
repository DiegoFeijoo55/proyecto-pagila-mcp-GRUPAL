from mcp_server.server import mcp
from mcp_server import tools


@mcp.tool()
def list_tables() -> list:
    return tools.list_tables()


@mcp.tool()
def describe_table(table_name: str) -> list:
    return tools.describe_table(table_name)


@mcp.tool()
def run_safe_query(query: str) -> list:
    return tools.run_safe_query(query)


if __name__ == "__main__":
    mcp.run()
