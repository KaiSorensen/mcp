# documentation for Python MCP servers SDK can be found at https://github.com/modelcontextprotocol/python-sdk/
# link to the general MCP protocol: https://github.com/modelcontextprotocol

# This is a barebones proof-of-concept example of an MCP server

## MY BIGGEST QUESTION
# QUESTION: How does the LLM know which methods to call? What informs its decision?
# ANSWER: Apparently, the LLM basically reads the function headers including its parameters, as well as the "docstrings".
# In Python, a docstring is the string immediately following the function definition. This convention is expected by the MCP protocol.
# So, to provide the LLM with better context, it is important to provide good docstrings for each function.


## UNDERSTANDING MCP SERVERS
# 1.  When you run this script, it will start an MCP server.
# 2.  When an MCP server is ran, it creates a JSON metadata object that describes the server's functions. The JSON metadata basically just presents the function headers and docstrings.
# 3.  When an LLM connects to the server, the server sends its metadata to the LLM.
# 4.  The LLM uses this JSON metadata to determine which methods to call, and intelligently chooses the best method to call (or none at all).

## MCP BASICS
# 1.  Resources: like getters
# 2.  Tools: functions that execute logic, call server-side actions (file modification, database writes, etc.)
# 3.  Prompts: (I'm not sure yet, but maybe it's just more context for how to handle a particular request?)



# pip install "mcp[cli]""
from mcp.server.fastmcp import FastMCP, Context

# Instantiate a minimal MCP server named 'POC'
mcp = FastMCP("Kai's MCP Server")

# -- Resource: Expose simple data
@mcp.tool("kai://kai_favorite_city")
def get_favorite_city() -> str:
    """This function gets Kai's favorite city."""
    return "Kai's favorite city is 'Miami'"

@mcp.tool("kai://kai_favorite_food")
def get_favorite_food() -> str:
    """This function gets Kai's favorite food."""
    return "Kai's favorite food is 'Cuban sandwiches'"

@mcp.tool("kai://sum")
def sum(a: int, b: int, c: int) -> int:
    """Sum three integers."""
    return a + b + c

# # -- Tool: Perform an action
# @mcp.tool()
# def echo(message: str) -> str:
#     """Echo back the provided message"""
#     return f"Echo: {message}"

# # -- Prompt: Provide a reusable template
# @mcp.prompt()
# def greet_prompt(name: str) -> str:
#     """Generate a greeting prompt for the LLM"""
#     return f"You are an assistant. Greet {name} enthusiastically!"

# -- Direct execution entrypoint
if __name__ == "__main__":
    print("Starting MCP server.")
    mcp.run(bro="fucking run")  # Blocks and listens for MCP client connections

# docker build --no-cache -t mcp . && docker run -p 8000:8000 mcp
