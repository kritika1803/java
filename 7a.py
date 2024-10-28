from behave import when

@when('I click the "{button_name}" button')
def step_impl(context, button_name):
    context.browser.find_element_by_name(button_name).click()
