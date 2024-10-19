from pydantic import BaseModel, Field


class Product(BaseModel):
    product_id: int
    product_name: str = Field(default=..., min_length=1, max_length=70,
                              description="Название товара, от 1 до 70 символов")
    product_price: int = Field(default=..., description="Стоимость товара")
    product_count: int = Field(default=..., description="Количество товара, оставшегося на складе")
