from application.repositories.categorization_repository import CategorizationRepository


class InMemoryCategorizationRepository(CategorizationRepository):
    def __init__(self):
        self._data = {}

    def find_by_id(self, categorization_id):
        return self._data.get(categorization_id)

    def save(self, categorization):
        self._data[categorization.id] = categorization
