from kopeechka import MailActivations
import logging

api = MailActivations("TOKEN")

logger = logging.getLogger("kopeechka")
logger.setLevel(logging.CRITICAL + 1)

print(api.user_balance().balance)
