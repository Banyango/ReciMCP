from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any

from wireup import abstract


@abstract
class RecipeClient(ABC):
    """Abstract base class for recipe API clients."""

    @abstractmethod
    def search_recipe_by_name(self, name: str) -> Dict[str, Any]:
        """Search meals by name.

        Args:
            name: The meal name to search for

        Returns:
            API response containing matching meals
        """
        pass

    @abstractmethod
    def list_recipes_by_first_letter(self, letter: str) -> Dict[str, Any]:
        """List all meals starting with a specific letter.

        Args:
            letter: Single letter (a-z)

        Returns:
            API response containing meals starting with the letter
        """
        pass

    @abstractmethod
    def lookup_recipe_by_id(self, meal_id: str) -> Dict[str, Any]:
        """Lookup full meal details by ID.

        Args:
            meal_id: The meal ID

        Returns:
            API response containing meal details
        """
        pass

    @abstractmethod
    def get_random_recipe(self) -> Dict[str, Any]:
        """Get a single random meal.

        Returns:
            API response containing a random meal
        """
        pass

    @abstractmethod
    def get_random_selection(self) -> Dict[str, Any]:
        """Get 10 random meals (Premium API only).

        Returns:
            API response containing 10 random meals
        """
        pass

    @abstractmethod
    def list_categories(self) -> Dict[str, Any]:
        """List all meal categories.

        Returns:
            API response containing all categories
        """
        pass

    @abstractmethod
    def get_latest_recipes(self) -> Dict[str, Any]:
        """Get latest meals (Premium API only).

        Returns:
            API response containing latest meals
        """
        pass

    @abstractmethod
    def list_all_categories(self) -> Dict[str, Any]:
        """List all category names."""
        pass

    @abstractmethod
    def list_all_areas(self) -> Dict[str, Any]:
        """List all area names."""
        pass

    @abstractmethod
    def list_all_ingredients(self) -> Dict[str, Any]:
        """List all ingredient names."""
        pass

    @abstractmethod
    def filter_by_ingredient(self, ingredient: str) -> Dict[str, Any]:
        """Filter meals by main ingredient.

        Args:
            ingredient: Ingredient name

        Returns:
            API response containing filtered meals
        """
        pass

    @abstractmethod
    def filter_by_multi_ingredients(self, ingredients: List[str]) -> Dict[str, Any]:
        """Filter by multiple ingredients (Premium API only).

        Args:
            ingredients: List of ingredient names

        Returns:
            API response containing filtered meals
        """
        pass

    @abstractmethod
    def filter_by_category(self, category: str) -> Dict[str, Any]:
        """Filter meals by category.

        Args:
            category: Category name

        Returns:
            API response containing filtered meals
        """
        pass

    @abstractmethod
    def filter_by_area(self, area: str) -> Dict[str, Any]:
        """Filter meals by area/region.

        Args:
            area: Area/region name

        Returns:
            API response containing filtered meals
        """
        pass

    @abstractmethod
    def get_recipe_image_url(self, image_path: str, size: str = "medium") -> str:
        """Get meal thumbnail image URL.

        Args:
            image_path: Original image path
            size: Image size (small, medium, large, preview)

        Returns:
            Full image URL
        """
        pass

    @abstractmethod
    def get_ingredient_image_url(self, ingredient: str, size: Optional[str] = None) -> str:
        """Get ingredient thumbnail image URL.

        Args:
            ingredient: Ingredient name
            size: Optional size suffix (small, medium, large)

        Returns:
            Full image URL
        """
        pass
