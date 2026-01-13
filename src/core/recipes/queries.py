from core.interfaces.recipe_client import RecipeClient
from core.recipes.response_models import RecipesResponseModel, RecipeResponseModel


class RecipeQueries:
    def __init__(self, client: RecipeClient):
        self.client = client

    def get_recipe_by_name(self, recipe_name: str) -> str:
        """Get a recipe by name.

        Args:
            recipe_name (str): The name of the recipe.
        """
        recipes = self.client.search_recipe_by_name(recipe_name)

        if not recipes.get("meals"):
            raise ValueError(f"No recipes found for name: {recipe_name}")

        model = RecipesResponseModel.model_validate(recipes)

        return model.model_dump_json()

    def get_recipe_by_id(self, recipe_id: int) -> str:
        """Get a recipe by ID.

        Args:
            recipe_id (int): The ID of the recipe.
        """
        recipe = self.client.lookup_recipe_by_id(str(recipe_id))

        if not recipe.get("meals"):
            raise ValueError(f"Recipe with ID {recipe_id} not found.")

        model = RecipeResponseModel.model_validate(recipe)

        return model.model_dump_json()
