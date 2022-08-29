class Error(Exception):
    
    def __init__(self, error, message, remedy):
        self.error = error
        self.message = message
        self.remedy = remedy
        super().__init__(message)


    def __str__(self):
        return f"""
        Error:
            {self.error}
        Details:
            {self.message}
        Remedy:
            {self.remedy}
        """
