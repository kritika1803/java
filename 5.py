from behave import given

@given('a product exists with name "{name}"')
def step_impl(context, name):
    context.product = create_fake_product(name=name)
    add_product_to_db(context.product)
