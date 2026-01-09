class AppException(Exception):
    def __init__(self, error_message, error_detail=None):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_detail = error_detail

    def __str__(self):
        if self.error_detail:
            return f"{self.error_message} | Details: {self.error_detail}"
        return self.error_message
