from UI_tests_aut.main.browsers_model.browsers import Browsers


class Chrome(Browsers):

    def __init__(self):
        self.browser_type = 'chrome'
        Browsers.__init__(self, self.browser_type)

    def get_browser_type(self):
        return self.browser_type
