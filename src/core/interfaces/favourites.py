from abc import ABC, abstractmethod

from wireup import abstract


@abstract
class FavouritesRepository(ABC):
    @abstractmethod
    def add_favourite(self, item_id: str) -> None:
        """Add an item to favourites by its ID.

        Args:
            item_id (str): The ID of the item to be added to favourites.
        """

    @abstractmethod
    def remove_favourite(self, item_id: str) -> None:
        """Remove an item from favourites by its ID.

        Args:
            item_id (str): The ID of the item to be removed from favourites.
        """

    @abstractmethod
    def list_favourites(self) -> list:
        """List all favourite items."""
