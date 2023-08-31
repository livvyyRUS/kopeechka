from aiohttp import ClientSession, ClientTimeout
from kopeechka.config import soft_id as sft_id


class AsyncMethods:
    def __init__(self, api_token: str):
        self.api_token: str = api_token
        self.default_query = {
            "token": self.api_token,
            "type": "JSON",
            "api": 2.0
        }
        self.timeout = ClientTimeout(total=10)

    async def user_balance(self, **kwargs) -> dict:
        query = {}
        query.update(self.default_query)
        query.update(kwargs)

        async with ClientSession() as session:
            response = await session.get("http://api.kopeechka.store/user-balance", params=query)
        return await response.json()

    async def mailbox_get_email(self, site: str, mail_type: str = "", regex: str = "",
                                soft_id: str = sft_id, investor: int = "", subject: str = "", password: int = "",
                                **kwargs) -> dict:
        query = {
            "site": site,
            "mail_type": mail_type,
            "regex": regex,
            "soft": soft_id,
            "investor": investor,
            "subject": subject,
            "password": password
        }

        query.update(self.default_query)
        query.update(kwargs)

        async with ClientSession(timeout=self.timeout) as session:
            response = await session.get("http://api.kopeechka.store/mailbox-get-email", params=query)
        return await response.json()

    async def mailbox_get_message(self, task_id: int, full: int = "", **kwargs) -> dict:
        query = {
            "id": task_id,
            "full": full
        }

        query.update(self.default_query)
        query.update(kwargs)

        async with ClientSession(timeout=self.timeout) as session:
            response = await session.get("http://api.kopeechka.store/mailbox-get-message", params=query)
        return await response.json()

    async def mailbox_cancel(self, task_id: int, **kwargs) -> dict:
        query = {
            "id": task_id
        }
        query.update(self.default_query)
        query.update(kwargs)

        async with ClientSession(timeout=self.timeout) as session:
            response = await session.get("http://api.kopeechka.store/mailbox-cancel", params=query)
        return await response.json()

    async def mailbox_reorder(self, site: str, email: str, regex: str = "", subject: str = "", password: int = "",
                              **kwargs) -> dict:
        query = {
            "site": site,
            "email": email,
            "regex": regex,
            "subject": subject,
            "password": password
        }
        query.update(self.default_query)
        query.update(kwargs)

        async with ClientSession(timeout=self.timeout) as session:
            response = await session.get("http://api.kopeechka.store/mailbox-reorder", params=query)
        return await response.json()

    async def mailbox_get_fresh_id(self, site: str, email: str, **kwargs) -> dict:
        query = {
            "site": site,
            "email": email
        }
        query.update(self.default_query)
        query.update(kwargs)

        async with ClientSession(timeout=self.timeout) as session:
            response = await session.get("http://api.kopeechka.store/mailbox-get-fresh-id", params=query)
        return await response.json()

    async def mailbox_get_domains(self, site: str = "", **kwargs) -> dict:
        query = {
            "site": site
        }
        query.update(self.default_query)
        query.update(kwargs)

        async with ClientSession(timeout=self.timeout) as session:
            response = await session.get("http://api.kopeechka.store/mailbox-get-domains", params=query)
        return await response.json()

    async def mailbox_zones(self, popular: int = "", zones: int = "", **kwargs) -> dict:
        query = {
            "popular": popular,
            "zones": zones
        }
        query.update(self.default_query)
        query.update(kwargs)

        async with ClientSession(timeout=self.timeout) as session:
            response = await session.get("https://api.kopeechka.store/mailbox-zones", params=query)
        return await response.json()
