from typing import Optional, Dict, Any, List
import httpx
from wireup import service

from core.interfaces.recipe_client import RecipeClient

@service
class MealDBClient(RecipeClient):
    """Client for TheMealDB API."""

    def __init__(self):
        self.api_key = "1"
        self.base_url = f"https://www.themealdb.com/api/json/v1/{self.api_key}"
        self.client = httpx.Client(timeout=30.0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def close(self):
        self.client.close()

    def search_recipe_by_name(self, name: str) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/search.php", params={"s": name})
        response.raise_for_status()
        return response.json()

    def list_recipes_by_first_letter(self, letter: str) -> Dict[str, Any]:
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Letter must be a single alphabetic character")
        response = self.client.get(f"{self.base_url}/search.php", params={"f": letter.lower()})
        response.raise_for_status()
        return response.json()

    def lookup_recipe_by_id(self, recipe_id: str) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/lookup.php", params={"i": recipe_id})
        response.raise_for_status()
        return response.json()

    def get_random_recipe(self) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/random.php")
        response.raise_for_status()
        return response.json()

    def get_random_selection(self) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/randomselection.php")
        response.raise_for_status()
        return response.json()

    def list_categories(self) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/categories.php")
        response.raise_for_status()
        return response.json()

    def get_latest_recipes(self) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/latest.php")
        response.raise_for_status()
        return response.json()

    def list_all_categories(self) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/list.php", params={"c": "list"})
        response.raise_for_status()
        return response.json()

    def list_all_areas(self) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/list.php", params={"a": "list"})
        response.raise_for_status()
        return response.json()

    def list_all_ingredients(self) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/list.php", params={"i": "list"})
        response.raise_for_status()
        return response.json()

    def filter_by_ingredient(self, ingredient: str) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/filter.php", params={"i": ingredient})
        response.raise_for_status()
        return response.json()

    def filter_by_multi_ingredients(self, ingredients: List[str]) -> Dict[str, Any]:
        ingredient_str = ",".join(ingredients)
        response = self.client.get(f"{self.base_url}/filter.php", params={"i": ingredient_str})
        response.raise_for_status()
        return response.json()

    def filter_by_category(self, category: str) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/filter.php", params={"c": category})
        response.raise_for_status()
        return response.json()

    def filter_by_area(self, area: str) -> Dict[str, Any]:
        response = self.client.get(f"{self.base_url}/filter.php", params={"a": area})
        response.raise_for_status()
        return response.json()

    def get_recipe_image_url(self, image_path: str, size: str = "medium") -> str:
        # If image_path is already a full URL, extract the path
        if image_path.startswith("http"):
            # Extract path from full URL
            image_path = image_path.split(".com")[-1]

        # Remove any existing size suffix
        if image_path.endswith(("/small", "/medium", "/large", "/preview")):
            image_path = "/".join(image_path.split("/")[:-1])

        base_url = f"https://www.themealdb.com{image_path}"

        if size == "preview":
            return f"{base_url}/preview"
        return f"{base_url}/{size}"

    def get_ingredient_image_url(self, ingredient: str, size: Optional[str] = None) -> str:
        # Replace spaces with underscores and convert to lowercase
        ingredient_name = ingredient.replace(" ", "_").lower()
        base_url = f"https://www.themealdb.com/images/ingredients/{ingredient_name}"

        if size:
            return f"{base_url}-{size}.png"
        return f"{base_url}.png"

