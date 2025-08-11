from uuid import UUID
from behave import *
from create_categorization import CreateCategorizationInput, CreateCategorization
from decimal import Decimal

from infra.repositories.categorization_repository import (
    InMemoryCategorizationRepository,
)

from domain.entities.global_categorization import GlobalCategorization


# add repository global
repository = InMemoryCategorizationRepository()


@given('an existing parent categorization with ID "1"')
def a(context):
    context.parent_categorization_data = {
        "id": "1",
        "name": "Parent Categorization",
        "budget": Decimal("10000"),
    }

    parent_categorization = GlobalCategorization(**context.parent_categorization_data)

    repository.save(parent_categorization)


@given("a categorization data")
def b(context):
    context.categorization_data = {}
    for row in context.table:
        value = row["value"]
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.startswith("[") and value.endswith("]"):
            value = eval(value)
        context.categorization_data[row["field"]] = value


@when('create a categorization "{type}" with the provided data')
def c(context, type: str):
    context.type = type
    input = CreateCategorizationInput(**context.categorization_data, type=type)
    create_categorization = CreateCategorization(repository)
    try:
        context.categorization_id = create_categorization.execute(input)
    except Exception as e:
        print(f"Error during categorization creation: {e}")
        context.error = e


@then("the output should contain the categorization ID")
def d(context):
    assert hasattr(context, "categorization_id")


@then("the categorization should be created successfully")
def e(context):
    categorization = repository.find_by_id(context.categorization_id)

    assert categorization is not None


@then("the categorization should be linked to its parent categorization")
def f(context):

    categorization = repository.find_by_id(context.categorization_id)
    parent_categorization = repository.find_by_id(
        context.parent_categorization_data["id"]
    )

    assert categorization is not None
    assert parent_categorization is not None
    assert categorization.parent_id == parent_categorization.id
    assert categorization in parent_categorization.children


@then("the categorization creation should fail")
def g(context):
    assert isinstance(context.error, Exception)


@then("the error message should indicate budget exceeds parent's budget")
def h(context):
    assert "Sum of children's budgets exceeds parent's budget" == str(context.error)
