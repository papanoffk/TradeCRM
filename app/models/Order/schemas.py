from pydantic import BaseModel, Field
from typing import Dict
from enum import Enum


class OrderStatus(str, Enum):
    is_ready = "Заказ доставлен"


class Order(BaseModel):
    order_id: int
    buyer_id: int = Field(default=..., description="Идентификатор покупателя, которому принадлежит заказ")
    order_list: Dict[str, int] = Field(default=..., description="Список покупок, оформленный словарем,"
                                                                " где ключ - product_id, а значение - need_count")
    order_status: OrderStatus = Field(default=..., description="Статус, в котором находится заказ")
    order_price: int = Field(default=..., description="Цена заказа с применением скидок")
    post_order_price: int = Field(default=..., description="Цена доставки с применением скидок")
