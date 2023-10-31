from kopeechka import MailActivations, KopeechkaApiError

api = MailActivations("TOKEN")


def main():
    try:
        ans_1 = api.user_balance()
        print(ans_1)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_2 = api.mailbox_get_email("vk.com")
        print(ans_2)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_3 = api.mailbox_get_message(ans_2.id, 1)
        print(ans_3)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_4 = api.mailbox_cancel(ans_2.id)
        print(ans_4)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_5 = api.mailbox_reorder("vk.com", ans_2.mail)
        print(ans_5)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_6 = api.mailbox_get_fresh_id("vk.com", ans_2.mail)
        print(ans_6)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_7 = api.mailbox_get_domains("vk.com")
        print(ans_7)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_8 = api.mailbox_zones(1, 1)
        print(ans_8)
    except KopeechkaApiError as e:
        print(e)


if __name__ == '__main__':
    main()
