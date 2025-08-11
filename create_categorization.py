from decimal import Decimal
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel

from domain.factory.categorization_factory import CategorizationFactory
from application.repositories.categorization_repository import CategorizationRepository


class CreateCategorizationInput(BaseModel):
    name: str
    type: str
    budget: Decimal
    parent_id: Optional[str] = None
    integration_data_id: Optional[UUID] = None
    groups: Optional[List[str]] = None


class CreateCategorization:

    def __init__(self, categorization_repository: CategorizationRepository):
        self.categorization_repository = categorization_repository

    def execute(self, input: CreateCategorizationInput) -> str:
        categorization = CategorizationFactory.create_categorization(
            input.type,
            name=input.name,
            budget=input.budget,
            parent_id=input.parent_id,
            integration_data_id=input.integration_data_id,
            groups=input.groups,
        )

        if input.parent_id:
            parent_categorization = self.categorization_repository.find_by_id(
                input.parent_id
            )

            if parent_categorization:
                parent_categorization.add_child(categorization)

        self.categorization_repository.save(categorization)

        return categorization.id
