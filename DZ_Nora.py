class Product:
    '''
    Product - класс для описания продукта; класс, представляющий товар, с атрибутами name (название товара) и price (цена товара).
    '''

    def __init__(self, name, price):
        self.name = name    # название продукта
        self.price = price  # цена продукта

    def __str__(self):
        return f'Product(name={self.name}, price={self.price})'

    def __repr__(self):
        return f'Product(name={self.name!r}, price={self.price!r})'

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return False


class Customer:
    '''
    Customer - класс, представляющий клиента, с атрибутами name (имя клиента) и orders (список заказов клиента).
    '''
    def __init__(self, name: str, orders: list):
        self.name = name
        self.orders = orders

    def __str__(self):
        return f'Customer(name={self.name}, orders_count={len(self.orders)})'

    def __repr__(self):
        return f'Customer(name={self.name!r}, orders={self.orders!r})'


class Order:
    '''
    Order - класс, представляющий заказ, с атрибутом products (список продуктов в заказе).
    методы класса в классе Order для подсчета общего количества заказов и общей суммы заказов для всех клиентов.
    '''

    total_orders = 0
    total_amount = 0

    def __init__(self, products: list):
        self.products = products
        Order.total_orders += 1
        Order.total_amount += self.calculate_order_total()

    def calculate_order_total(self):
        return sum(product.price for product in self.products)

    def get_order_total(self):
        return len(self.products)

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    @classmethod
    def get_total_amount(cls):
        return cls.total_amount

    def __str__(self):
        return f'Order(total_amount={self.calculate_order_total()}, products_count={len(self.products)})'

    def __repr__(self):
        return f'Order(products={self.products!r})'


class Discount:
    '''
    Discount - класс для применения скидок, с атрибутами description (описание скидки) и discount_percent (процент скидки).
    '''

    def __init__(self, description: str, discount_percent: int):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price: float, discount_percent: int) -> float:
        '''
        Применяет скидку к цене и возвращает итоговую стоимость.
        '''
        return price * (1 - discount_percent / 100)

    @staticmethod
    def seasonal_discount(price: float) -> float:
        '''
        Применяет сезонную скидку (например, 10%) и возвращает итоговую стоимость.
        '''
        return Discount.apply_discount(price, 10)

    @staticmethod
    def promo_code_discount(price: float, promo_discount_percent: int) -> float:
        '''
        Применяет скидку по промокоду и возвращает итоговую стоимость.
        '''
        return Discount.apply_discount(price, promo_discount_percent)

    def __str__(self):
        return f'Discount(description={self.description}, discount_percent={self.discount_percent}%)'

    def __repr__(self):
        return f'Discount(description={self.description!r}, discount_percent={self.discount_percent!r})'


# Продукты
milk = Product("Colun", 1100)
apples = Product("Red Delicious", 1700)
oranges = Product("Valencia", 1500)
bread = Product("Baguette", 800)
cheese = Product("Gouda", 2000)

# Клиенты
person1 = Customer('Nora', orders=[])
person2 = Customer('Maria Paz', orders=[])
person3 = Customer('Maria José', orders=[])

# Заказы
order1 = Order([apples, oranges])  # сумма: 3200
order2 = Order([milk, apples, oranges])  # сумма: 4300
order3 = Order([bread, cheese])  # сумма: 2800

# Добавление заказов к клиентам
person1.orders.append(order1)
person2.orders.append(order2)
person3.orders.append(order3)

# Скидки
seasonal_discount = Discount('Сезонная скидка', 10)
promo_discount = Discount('Скидка по промокоду', 20)

# Применение скидок
final_price_order1 = seasonal_discount.apply_discount(order1.calculate_order_total(), seasonal_discount.discount_percent)
final_price_order2 = promo_discount.apply_discount(order2.calculate_order_total(), promo_discount.discount_percent)
final_price_order3 = seasonal_discount.apply_discount(order3.calculate_order_total(), seasonal_discount.discount_percent)

# Вывод финальных цен после применения скидок
print(f"Итоговая цена за заказ 1 после сезонной скидки: {final_price_order1}")
print(f"Итоговая цена за заказ 2 после скидки по промокоду: {final_price_order2}")
print(f"Итоговая цена за заказ 3 после сезонной скидки: {final_price_order3}")

# Подсчет общего количества заказов и общей суммы всех заказов
total_orders = Order.get_total_orders()
total_amount = Order.get_total_amount()

print(f"Общее количество заказов: {total_orders}")
print(f"Общая сумма всех заказов: {total_amount}")

# Вывод информации о клиентах, заказах и продуктах
print(person1)
print(person2)
print(person3)

print(order1)
print(order2)
print(order3)

print(milk)
print(apples)
print(oranges)
print(bread)
print(cheese)




