class KopeechkaApiError(Exception):
    def __init__(self, status: str, value: str):
        self.status = status
        self.value = value

    def __str__(self):
        return self.value


class TimeOut(Exception):
    def __str__(self):
        return "Timed out"


def catch_error(json_data: dict, logger):
    if json_data.get("status") == "ERROR":
        value = json_data.get("value")
        logger.error(f'Error catched with value "{value}"')
        raise KopeechkaApiError(**json_data)
