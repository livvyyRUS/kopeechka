from kopeechka import MailActivations

api = MailActivations("TOKEN")

print(api.user_balance().balance)