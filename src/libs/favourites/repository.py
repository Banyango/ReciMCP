import shelve

from wireup import service

from core.interfaces.favourites import FavouritesRepository

@service
class FavouritesRepository(FavouritesRepository):
    def add_favourite(self, item_id: str) -> None:
        with shelve.open("favourites") as db:
            shelved_favourites = db["favourites"]

            if shelved_favourites is None:
                shelved_favourites = []

            shelved_favourites.append(item_id)

            db["favourites"] = shelved_favourites


    def remove_favourite(self, item_id: str) -> None:
        with shelve.open("favourites") as db:
            shelved_favourites = db["favourites"]

            if shelved_favourites is None:
                shelved_favourites = []
            else:
                shelved_favourites.remove(item_id)

            db["favourites"] = shelved_favourites

    def list_favourites(self) -> list[str]:
        with shelve.open("favourites") as db:
            shelved_favourites = db.get("favourites", [])

            if shelved_favourites is None:
                shelved_favourites = []

            return shelved_favourites