from core.interfaces.favourites import FavouritesRepository


class AddFavouriteCommand:
    def __init__(self, repository: FavouritesRepository, item: str):
        self.repository = repository
        self.item = item

    def execute(self):
        self.repository.add_favourite(self.item)