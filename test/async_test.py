from kopeechka import AsyncMailActivations, KopeechkaApiError
import asyncio

api = AsyncMailActivations("TOKEN")


async def main():
    try:
        ans_1 = await api.user_balance()
        print(ans_1)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_2 = await api.mailbox_get_email("vk.com")
        print(ans_2)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_3 = await api.mailbox_get_message(ans_2.id, 1)
        print(ans_3)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_4 = await api.mailbox_cancel(ans_2.id)
        print(ans_4)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_5 = await api.mailbox_reorder("vk.com", ans_2.mail)
        print(ans_5)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_6 = await api.mailbox_get_fresh_id("vk.com", ans_2.mail)
        print(ans_6)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_7 = await api.mailbox_get_domains("vk.com")
        print(ans_7)
    except KopeechkaApiError as e:
        print(e)

    try:
        ans_8 = await api.mailbox_zones(1, 1)
        print(ans_8)
    except KopeechkaApiError as e:
        print(e)


if __name__ == '__main__':
    asyncio.run(main())
