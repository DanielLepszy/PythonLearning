# -- FILE: features/steps/remove_all_items.py

from behave import given, when, then, step
from selenium import webdriver


@given('standard user log in to app')
def given_impl(context):


@when('add Sauce Labs backpack and bike light to card')
def given_impl(context):
    print('xx')

@when('user click on shopping trolley icon to open his card')
def when_impl(context):  # -- NOTE: number is converted into integer
   assert True
    # assert number > 1 or number == 0
    # context.tests_count = number

@when('remove each items from card')
def when_impl(context):  # -- NOTE: number is converted into integer
    assert True

@when('click CONTINUE SHOPPING button')
def when_impl(context):  # -- NOTE: number is converted into integer
    assert True

@then('system back to inventory page')
def step_impl(context):

    assert True
    # assert context.failed is False
    # assert context.tests_count >= 0

@then('items counter icon disappeared')
def step_impsl(context):
    assert True