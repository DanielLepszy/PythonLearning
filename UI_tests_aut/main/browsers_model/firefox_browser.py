from UI_tests_aut.browsers_model.browsers import Browsers


class Firefox(Browsers):

    def __init__(self):
        self.browser_type = 'firefox'
        Browsers.__init__(self, self.browser_type)

    def get_browser_type(self):
        return self.browser_type
