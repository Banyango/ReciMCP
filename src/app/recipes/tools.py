from wireup.integration.starlette import inject

from app.container import container
from core.interfaces.recipe_client import RecipeClient
from core.recipes.queries import RecipeQueries


@inject
async def get_recipe_by_name(recipe_name: str) -> str:
    """Get a recipe by name tool.

    Args:
        recipe_name (str): The name of the recipe.
    """
    recipe_client = await container.get(RecipeClient)

    tool = RecipeQueries(recipe_client)

    return tool.get_recipe_by_name(recipe_name)


@inject
async def get_recipe_by_id(recipe_id: int) -> str:
    """
    Get a recipe by ID tool.

    Args:
        recipe_id (int): The ID of the recipe.
    """
    recipe_client = await container.get(RecipeClient)

    tool = RecipeQueries(recipe_client)

    return tool.get_recipe_by_id(recipe_id)