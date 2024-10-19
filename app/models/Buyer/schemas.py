from pydantic import BaseModel, Field
from types import FunctionType
from typing import Optional


class Privilege(BaseModel):
    privilege_id: int
    privilege_name: str = Field(default=..., min_length=1, max_length=70,
                                description="Название привилегии, от 1 до 70 символов")
    privilege_func: [FunctionType, None] = Field(default=None, description="Функция, которую применят к цене привилегия")


class Buyer(BaseModel):
    buyer_id: int
    name: str = Field(default=..., min_length=1, max_length=50, description="Имя покупателя, от 1 до 50 символов")
    lastname: str = Field(default=..., min_length=1, max_length=70,
                          description="Фамилия покупателя, от 1 до 70 символов")
    surname: str = Field(default=..., min_length=1, max_length=70,
                         description="Отчество покупателя, от 1 до 70 символов")
    address: str = Field(default=..., description="Адрес покупателя")
    index: str = Field(default=..., description="Индекс адреса покупателя")
    link: str = Field(default=..., description="Ссылка на соцсеть покупателя для связи")
    privilege: Privilege = Field(default=..., description="Привилегии покупателя")
