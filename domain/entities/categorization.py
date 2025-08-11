from pydantic import BaseModel, Field

from decimal import Decimal

from typing import Optional


class Categorization(BaseModel):
    id: str
    name: str
    budget: Decimal
    parent_id: Optional[str] = None
    children: list = Field(default_factory=list)

    def add_child(self, child_categorization):
        # valido se o children é None e inicializo como lista vazia
        if self.children is None:
            self.children = []

        # adiciono o child_categorization à lista de children
        self.children.append(child_categorization)

        # agora vou validar se a soma dos orçamentos dos filhos não ultrapassa o orçamento do pai
        if not self.validate_budget():
            raise ValueError("Sum of children's budgets exceeds parent's budget")

    def validate_budget(self):
        total_budget = sum(child.budget for child in self.children)

        return total_budget <= self.budget
