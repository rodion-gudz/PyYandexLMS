class AuthError(Exception):
    pass


class ApiException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f"API Error: {self.code} - {self.message}"
