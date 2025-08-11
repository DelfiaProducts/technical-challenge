from abc import ABC, abstractmethod


class CategorizationRepository(ABC):
    @abstractmethod
    def find_by_id(self, categorization_id):
        pass

    @abstractmethod
    def save(self, categorization):
        pass
