#!/usr/bin/env python3
"""
Simple MCP Boilerplate Server
Returns "hello world" as a basic example.
"""

from fastmcp import FastMCP
from fastapi.responses import JSONResponse
from fastapi import Request

# Create the MCP server
PORT = 28080
HOST = "0.0.0.0"

mcp = FastMCP("MCP Boilerplate", json_response=True, port=PORT, host=HOST)

# ============================================================================
# FastMCP Decorators and Methods
# ============================================================================

# 1. @mcp.tool() - TOOLS
#    What it does: Registers functions as callable actions that LLMs/clients can invoke.
#    Use case: When you want the LLM to perform actions (e.g., send emails, 
#              process data, make API calls, execute commands).
#    Example: A tool to search the web, send notifications, or update a database.
@mcp.tool()
def hello_world() -> str:
    """Returns a simple hello world message."""
    return "hello world"

# Tool with background task support
# @mcp.tool(task=True)  # Enable background execution
# async def long_running_task() -> str:
#     """A task that can run in the background."""
#     return "Task completed"

# 2. @mcp.resource() - RESOURCES
#    What it does: Exposes read-only data sources that LLMs/clients can read/access.
#    Use case: When you want to provide data to the LLM (e.g., files, configs,
#              database content, API responses) without allowing modifications.
#    Example: Reading a file, fetching user data, accessing configuration settings.
#    Note: Resources are read-only - they provide information but don't modify state.
# @mcp.resource("resource://greeting")
# def get_greeting() -> str:
#     """Provides a greeting message."""
#     return "Hello from FastMCP Resources!"

# Resource template with parameters
# @mcp.resource("data://{id}")
# def get_data(id: str) -> dict:
#     """Get data by ID."""
#     return {"id": id, "value": "data"}

# 3. @mcp.prompt() - PROMPTS
#    What it does: Defines reusable prompt templates that LLMs can fetch and use.
#    Use case: When you want to provide pre-written prompts or prompt templates
#              that guide the LLM's behavior or provide context.
#    Example: System prompts, instruction templates, or context-setting messages.
#    Note: Prompts are templates that can be parameterized and reused.
# @mcp.prompt()
# def system_prompt() -> str:
#     """System prompt for the assistant."""
#     return "You are a helpful assistant."

# Prompt with arguments
# @mcp.prompt()
# def user_prompt(name: str) -> str:
#     """Personalized prompt."""
#     return f"Hello, {name}!"

# 4. @mcp.custom_route() - Add custom HTTP endpoints (outside MCP protocol)
@mcp.custom_route('/health', methods=['GET'])
async def health_check(request: Request):
    """Custom route endpoint"""
    return JSONResponse({
        'status': 'ok',
        'transport': 'streamableHttp',
    })

# Additional custom routes
# @mcp.custom_route('/api/status', methods=['GET', 'POST'])
# async def api_status(request: Request):
#     """Another custom endpoint."""
#     return JSONResponse({"status": "running"})

# ============================================================================
# Other available methods on mcp instance:
# ============================================================================
# - mcp.add_resource(resource) - Manually add resources
# - mcp.add_tool(tool) - Manually add tools
# - mcp.add_prompt(prompt) - Manually add prompts
# - mcp.run() - Start the server (with various transport options)
# - mcp.http_app() - Get the Starlette app for custom deployment


if __name__ == "__main__":
    # FastMCP supports 4 transport types:
    
    # 1. stdio transport (default) - Standard Input/Output for local subprocess communication
    # mcp.run()  # or mcp.run(transport='stdio')
    
    # 2. http transport - Basic HTTP transport
    # mcp.run(transport='http')
    
    # 3. streamable-http transport - Recommended for production, supports bidirectional streaming
    mcp.run(transport='streamable-http')
    
    # 4. sse transport - Server-Sent Events (legacy, maintained for backward compatibility)
    # mcp.run(transport='sse')
