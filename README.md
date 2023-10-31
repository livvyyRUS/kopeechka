# kopeechka

**kopeechka** - This module is a representation of the kopeechka.store API in Python

**API documentation RUS** [ https://link.kopeechka.store/CzXxp6?lang=ru&k=API]( https://link.kopeechka.store/CzXxp6?lang=ru&k=API)

**API documentation ENG** [https://link.kopeechka.store/CzXxp6?lang=en&k=API](https://link.kopeechka.store/CzXxp6?lang=en&k=API)

# Installation

Install the current version with pip:

```commandline
pip install kopeechka
```

## Usage

You can get a token in your personal account on the kopeechka.store website

```python
from kopeechka import MailActivations

api = MailActivations(api_token="TOKEN")
```

## Logger
You can set logger with your settings

```python
from kopeechka import Logger, MailActivations

new_logger = Logger() # In the arguments you can set the settings

api = MailActivations(api_token="TOKEN", logger=new_logger)
```

You also can disable a logger
```python
import logging

logger = logging.getLogger("kopeechka")
logger.setLevel(logging.CRITICAL + 1)
```

## Exception handling

You can import KopeechkaApiError to catch errors
To catching timeout error import TimeOut

**Example:**
```python
from kopeechka import KopeechkaApiError, MailActivations, TimeOut

api = MailActivations(api_token="WRONG_TOKEN")

try:
    api.user_balance()
except KopeechkaApiError as e:
    print(e) # -> BAD_TOKEN
except TimeOut as e:
    print(e) # -> If it timed out, it return "Timed out"
```
## Types

You can import all types from kopeechka or kopeechka.kopeechka_types

## Sync methods

You can import class to work with methods from kopeechka
```python
from kopeechka import Methods

api = Methods(api_token="TOKEN")
```

## Sync example

```python
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

```

## Async methods

You can import class to work with async methods from kopeechka
```python
from kopeechka import AsyncMethods

api = AsyncMethods(api_token="TOKEN")
```
## Async example

```python
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

```