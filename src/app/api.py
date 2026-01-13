from fastapi import FastAPI
from fastmcp import FastMCP
from fastmcp.tools import Tool
from wireup.integration.starlette import setup

from app.config import APIConfig
from app.container import container
from app.favourites.tools import create_favourite_tool, remove_favourite_tool, list_favourites_tool

from app.recipes.tools import get_recipe_by_name, get_recipe_by_id


def create_api(config: APIConfig) -> FastAPI:
    """Create the FastAPI application with MCP integration.

    Args:
        config (APIConfig): The API configuration.
    """
    mcp = FastMCP("My MCP Server")
    mcp_app = mcp.http_app(path='/mcp')

    setup(container, mcp_app)

    app = FastAPI(title="ReciMCPe", lifespan=mcp_app.lifespan)
    app.mount("/api", mcp_app)

    mcp.add_tool(Tool.from_function(get_recipe_by_name))
    mcp.add_tool(Tool.from_function(get_recipe_by_id))

    mcp.add_tool(Tool.from_function(create_favourite_tool))
    mcp.add_tool(Tool.from_function(remove_favourite_tool))
    mcp.add_tool(Tool.from_function(list_favourites_tool))

    return app
