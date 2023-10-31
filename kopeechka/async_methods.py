from aiohttp import ClientSession, ClientTimeout
from asyncio.exceptions import TimeoutError
from kopeechka.config import sft_id, default_logger
from kopeechka.error import TimeOut
from kopeechka.module_log import Logger
import asyncio


class AsyncMethods:
    def __init__(self, api_token: str, timeout: int = 5, logger: Logger = default_logger):
        self.api_token: str = api_token
        self.default_query = {
            "token": self.api_token,
            "type": "JSON",
            "api": 2.0
        }
        self.timeout = ClientTimeout(total=timeout)
        self.logger = logger
        self.valid_token()

    def valid_token(self):
        self.logger.debug("Validating a API-token")
        asyncio.run(self.user_balance())

    async def request(self, url: str = "", params: dict = None):
        params.update(self.default_query)

        async with ClientSession(timeout=self.timeout) as session:
            response = await session.get(url=url, params=params)
        try:
            self.logger.debug(f'A request was sent to the url "{url}" with the parameters {params} and it returned {await response.json()}')
        except TimeoutError:
            raise TimeOut from None
        return response

    async def user_balance(self, **kwargs) -> dict:
        query = {
            **kwargs
        }
        response = await self.request("http://api.kopeechka.store/user-balance", params=query)
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
            "password": password,
            **kwargs
        }

        response = await self.request("http://api.kopeechka.store/mailbox-get-email", params=query)
        return await response.json()

    async def mailbox_get_message(self, task_id: int, full: int = "", **kwargs) -> dict:
        query = {
            "id": task_id,
            "full": full,
            **kwargs
        }

        response = await self.request("http://api.kopeechka.store/mailbox-get-message", params=query)
        return await response.json()

    async def mailbox_cancel(self, task_id: int, **kwargs) -> dict:
        query = {
            "id": task_id,
            **kwargs
        }

        response = await self.request("http://api.kopeechka.store/mailbox-cancel", params=query)
        return await response.json()

    async def mailbox_reorder(self, site: str, email: str, regex: str = "", subject: str = "", password: int = "",
                              **kwargs) -> dict:
        query = {
            "site": site,
            "email": email,
            "regex": regex,
            "subject": subject,
            "password": password,
            **kwargs
        }

        response = await self.request("http://api.kopeechka.store/mailbox-reorder", params=query)
        return await response.json()

    async def mailbox_get_fresh_id(self, site: str, email: str, **kwargs) -> dict:
        query = {
            "site": site,
            "email": email,
            **kwargs
        }

        response = await self.request("http://api.kopeechka.store/mailbox-get-fresh-id", params=query)
        return await response.json()

    async def mailbox_get_domains(self, site: str = "", **kwargs) -> dict:
        query = {
            "site": site,
            **kwargs
        }

        response = await self.request("http://api.kopeechka.store/mailbox-get-domains", params=query)
        return await response.json()

    async def mailbox_zones(self, popular: int = "", zones: int = "", **kwargs) -> dict:
        query = {
            "popular": popular,
            "zones": zones,
            **kwargs
        }

        response = await self.request("https://api.kopeechka.store/mailbox-zones", params=query)
        return await response.json()
