from core.interfaces.favourites import FavouritesRepository


class RemoveFavouriteCommand:
    def __init__(self, repository: FavouritesRepository, item: str):
        self.repository = repository
        self.item = item

    def execute(self):
        self.repository.remove_favourite(self.item)