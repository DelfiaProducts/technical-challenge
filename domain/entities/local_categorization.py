from uuid import UUID
from .categorization import Categorization


class LocalCategorization(Categorization):
    integration_data_id: UUID
    groups: list = []
