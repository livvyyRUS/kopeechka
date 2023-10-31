from dataclasses import dataclass

from typing import List


@dataclass
class UserBalance:
    status: str
    balance: float


@dataclass
class GetEmail:
    status: str
    id: int
    mail: str


@dataclass
class GetMessage:
    status: str
    value: str
    fullmessage: str


@dataclass
class Status:
    status: str


@dataclass
class GetTaskId:
    status: str
    id: int


@dataclass
class Domains:
    status: str
    count: int
    domains: List[str]


@dataclass
class Zone:
    name: str
    cost: int


@dataclass
class Popular:
    name: str
    cost: int
    count: int


@dataclass
class MailboxZones:
    status: str
    zones: List[Zone] = None
    popular: List[Popular] = None
