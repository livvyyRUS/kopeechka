class KopeechkaApiError(Exception):
    def __init__(self, status: str, value: str):
        self.status = status
        self.value = value

    def __str__(self):
        return self.value


def catch_error(json_data: dict):
    if json_data.get("status") == "ERROR":
        raise KopeechkaApiError(**json_data)
