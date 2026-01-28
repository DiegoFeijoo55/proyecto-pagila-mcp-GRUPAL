from mcp_server.tools import MCPTools


class MCPServer:
    def __init__(self):
        self.tools = MCPTools()

    def handle_request(self, tool_name: str, **kwargs):
        if not hasattr(self.tools, tool_name):
            raise ValueError(f"Tool no disponible: {tool_name}")

        tool = getattr(self.tools, tool_name)
        return tool(**kwargs)
