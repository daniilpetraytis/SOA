class Error(Exception):
    def __init__(self, internal_code=0, response_code=500, text=""):
        self.text = text
        self.internal_code = internal_code
        self.response_code = response_code

    def __str__(self):
        return self.text


class Redirect(Exception):
    def __init__(self, path="/"):
        self.path = path

    def __str__(self):
        return self.path


class NotFoundError(Error):
    def __init__(self, internal_code=None, text=""):
        super().__init__(internal_code, 404, text)
