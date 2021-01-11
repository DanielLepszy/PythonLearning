import allure

from test.base.test_case_base import TestCaseBase


def pytest_exception_interact(node, call, report):
    if report.failed:
        allure.attach(TestCaseBase.get_driver().get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
