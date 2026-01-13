from pydantic import BaseModel


class RecipeResponseModel(BaseModel):
    idMeal: str
    strMeal: str
    strCategory: str
    strArea: str
    strInstructions: str
    strMealThumb: str
    strTags: str | None
    strYoutube: str | None
    strIngredient1: str | None
    strIngredient2: str | None
    strIngredient3: str | None
    strIngredient4: str | None
    strIngredient5: str | None
    strIngredient6: str | None
    strIngredient7: str | None
    strIngredient8: str | None
    strIngredient9: str | None
    strIngredient10: str | None
    strIngredient11: str | None
    strIngredient12: str | None
    strIngredient13: str | None
    strIngredient14: str | None
    strIngredient15: str | None
    strIngredient16: str | None
    strIngredient17: str | None
    strIngredient18: str | None
    strIngredient19: str | None
    strIngredient20: str | None
    strMeasure1: str | None
    strMeasure2: str | None
    strMeasure3: str | None
    strMeasure4: str | None
    strMeasure5: str | None
    strMeasure6: str | None
    strMeasure7: str | None
    strMeasure8: str | None
    strMeasure9: str | None
    strMeasure10: str | None
    strMeasure11: str | None
    strMeasure12: str | None
    strMeasure13: str | None
    strMeasure14: str | None
    strMeasure15: str | None
    strMeasure16: str | None
    strMeasure17: str | None
    strMeasure18: str | None
    strMeasure19: str | None
    strMeasure20: str | None
    strSource: str | None


class RecipesResponseModel(BaseModel):
    meals: list[RecipeResponseModel]
