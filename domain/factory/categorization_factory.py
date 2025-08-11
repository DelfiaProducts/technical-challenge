from uuid import uuid4

from domain.entities.global_categorization import GlobalCategorization
from domain.entities.local_categorization import LocalCategorization


class CategorizationFactory:

    @staticmethod
    def create_categorization(categorization_type, **kwargs):
        id = str(uuid4())

        if categorization_type == "global":
            return GlobalCategorization(id=id, **kwargs)

        if categorization_type == "local":
            return LocalCategorization(id=id, **kwargs)

        raise ValueError(f"Unknown categorization type: {categorization_type}")
