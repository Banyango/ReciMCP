from wireup.integration.starlette import inject

from app.container import container
from core.favourites.add_favourite_command import AddFavouriteCommand
from core.interfaces.favourites import FavouritesRepository

@inject
async def create_favourite_tool(meal_id: str) -> str:
    """Create a favourite meal tool.

    Args:
        meal_id (str): The ID of the meal.
    """

    repository = container.get(FavouritesRepository)

    AddFavouriteCommand(repository, meal_id).execute()

    return f"Meal with ID {meal_id} has been added to favourites."

@inject
async def remove_favourite_tool(meal_id: str) -> str:
    """Remove a favourite meal tool.

    Args:
        meal_id (str): The ID of the meal.
    """

    repository = container.get(FavouritesRepository)

    repository.remove_favourite(meal_id)

    return f"Meal with ID {meal_id} has been removed from favourites."

@inject
async def list_favourites_tool() -> str:
    """List all favourite meals tool."""
    repository = await container.get(FavouritesRepository)

    favourites = repository.list_favourites()

    return f"Favourite meals: {', '.join(favourites)}"