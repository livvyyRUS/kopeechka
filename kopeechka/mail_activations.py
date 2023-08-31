from .methods import Methods
from kopeechka.config import soft_id as sft_id
from kopeechka.kopeechka_types import UserBalance, GetEmail, GetMessage, Status, GetTaskId, Domains, MailboxZones, Zone, Popular
from kopeechka.error import catch_error


class MailActivations(Methods):
    def __init__(self, api_token: str):
        super().__init__(api_token)

    def user_balance(self,
                     **kwargs
                     ) -> UserBalance:
        json_data = super().user_balance(**kwargs)
        catch_error(json_data)
        return UserBalance(**json_data)

    def mailbox_get_email(self,
                          site: str,
                          mail_type: str = "",
                          regex: str = "",
                          soft_id: str = sft_id,
                          investor: int = "",
                          subject: str = "",
                          password: int = "",
                          **kwargs
                          ) -> GetEmail:
        json_data = super().mailbox_get_email(site,
                                              mail_type,
                                              regex,
                                              soft_id,
                                              investor,
                                              subject,
                                              password,
                                              **kwargs
                                              )
        catch_error(json_data)
        return GetEmail(**json_data)

    def mailbox_get_message(self,
                            task_id: int,
                            full: int = "",
                            **kwargs
                            ) -> GetMessage:
        json_data = super().mailbox_get_message(task_id, full, **kwargs)
        catch_error(json_data)
        return GetMessage(**json_data)

    def mailbox_cancel(self,
                       task_id: int,
                       **kwargs
                       ) -> Status:
        json_data = super().mailbox_cancel(task_id, **kwargs)
        catch_error(json_data)
        return Status(**json_data)

    def mailbox_reorder(self,
                        site: str,
                        email: str,
                        regex: str = "",
                        subject: str = "",
                        password: int = "",
                        **kwargs
                        ) -> GetEmail:
        json_data = super().mailbox_reorder(site, email, regex, subject, password, **kwargs)
        catch_error(json_data)
        return GetEmail(**json_data)

    def mailbox_get_fresh_id(self,
                             site: str,
                             email: str,
                             **kwargs
                             ) -> GetTaskId:
        json_data = super().mailbox_get_fresh_id(site, email)
        catch_error(json_data)
        return GetTaskId(**json_data)

    def mailbox_get_domains(self,
                            site: str = "",
                            **kwargs
                            ) -> Domains:
        json_data = super().mailbox_get_domains(site, **kwargs)
        catch_error(json_data)
        return Domains(**json_data)

    def mailbox_zones(self,
                      popular: int = "",
                      zones: int = "",
                      **kwargs
                      ) -> MailboxZones:
        json_data = super().mailbox_zones(popular, zones)
        catch_error(json_data)
        return MailboxZones(json_data.get("status"),
                            zones=[Zone(**x) for x in json_data.get("zones")] if json_data.get("zones") else None,
                            popular=[Popular(**x) for x in json_data.get("popular")] if json_data.get(
                                "popular") else None)
