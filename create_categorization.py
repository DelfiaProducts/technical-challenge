from decimal import Decimal
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel


class CreateCategorizationInput(BaseModel):
    name: str
    type: str
    budget: Decimal
    parent_id: Optional[str] = None
    integration_data_id: Optional[UUID] = None
    groups: Optional[List[str]] = None


class CreateCategorization:

    def execute(self, input: CreateCategorizationInput) -> str:
        pass
