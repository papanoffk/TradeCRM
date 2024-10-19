# TradeCRM

## Сущности
1) Покупатель (Buyer)
   - Идентификатор покупателя (buyer_id) - int UUID
   - Имя (name) - str
   - Фамилия (lastname) - str
   - Отчество (surname) - str
   - Адрес (address) - str
   - Индекс (index) - str
   - Ссылка на соцсети (link) - str
   - Привилегии (privilege) - Privilege

2) Товар (Product)
   - Идентификатор товара (product_id) - str
   - Название (product_name) - str
   - Цена (product_price) - int
   - Доступное количество (product_count) - int

3) Заказ (Order)
   - Идентификатор заказа (order_id) - int
   - Идентификатор покупателя (buyer_id) - int
   - Список продуктов (order_list) - dict(product_id, need_count)
   - Статус заказа (order_status) - OrderStatus
   - Стоимость заказа (order_price) - int
   - Стоимость доставки (post_order_price) - int

4) Привилегия (Privilege)
   - Идентификатор привилегии (privilege_id) - int
   - Название привилегии (privilege_name) - str
   - Функция привилегии (privilege_func) - function

5) Статус заказа (OrderStatus) Класс-перечисление str, Enum
   - Пока непонятно