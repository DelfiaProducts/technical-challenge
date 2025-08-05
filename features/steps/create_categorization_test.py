from uuid import UUID
from behave import *
from create_categorization import CreateCategorizationInput, CreateCategorization


@given('an existing parent categorization with ID "1"')
def step_impl(context):
    context.parent_categorization_data = {
        "id": "1",
        "name": "Parent Categorization",
        "budget": "10000",
    }


@given("a categorization data")
def step_impl(context):
    context.categorization_data = {}
    for row in context.table:
        value = row["value"]
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.startswith("[") and value.endswith("]"):
            value = eval(value)
        context.categorization_data[row["field"]] = value


@when('create a categorization "{type}" with the provided data')
def step_impl(context, type: str):
    context.type = type
    input = CreateCategorizationInput(**context.categorization_data, type=type)
    create_categorization = CreateCategorization()
    try:
        context.categorization_id = create_categorization.execute(input)
    except Exception as e:
        context.error = e


@then("the output should contain the categorization ID")
def step_impl(context):
    assert hasattr(context, "categorization_id")


@then("the categorization should be created successfully")
def step_impl(context):
    raise NotImplementedError("STEP: the categorization should be created successfully")


@then("the categorization should be linked to its parent categorization")
def step_impl(context):
    raise NotImplementedError(
        "STEP: Then the categorization should be linked to its parent categorization"
    )


@then("the categorization creation should fail")
def step_impl(context):
    assert isinstance(context.error, Exception)


@then("the error message should indicate budget exceeds parent's budget")
def step_impl(context):
    assert "Sum of children's budgets exceeds parent's budget" == str(context.error)
