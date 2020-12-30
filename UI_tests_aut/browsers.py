class Browsers:

    def get_browser_type(self):
        return self.browser_type

    def open_browser(self):
        pass

    def __init__(self, browser_type) -> None:
        self.browser_type = browser_type
