"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999)

    def test_product_check_quantity_full(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)

    def test_product_check_quantity_negative(self, product):
        # TODO напишите проверки на метод check_quantity
        assert not product.check_quantity(1001)

    def test_product_buy_part(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900

    def test_product_buy_full(self, product):
        # TODO напишите проверки на метод buy
        product.buy(1000)
        assert product.quantity == 0

    def test_product_buy_two_times(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900
        product.buy(100)
        assert product.quantity == 800

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError): assert product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_999_1000(self, product, cart):
        cart.add_product(buy_count=999, product=product)
        assert cart.products[product] == 999
        cart.add_product(buy_count=1000, product=product)
        assert cart.products[product] == 1999

    def test_add_product_1001(self, product, cart):
        assert not cart.add_product(buy_count=1001, product=product)

    def test_remove_product_with_int(self, product, cart):
        cart.add_product(buy_count=100, product=product)
        cart.remove_product(remove_count=100, product=product)
        assert len(cart.products) == 0

    def test_remove_product_without_int(self, product, cart):
        cart.add_product(buy_count=1000, product=product)
        cart.remove_product(product=product)
        assert len(cart.products) == 0

    def test_remove_product_part(self, product, cart):
        cart.add_product(buy_count=1000, product=product)
        cart.remove_product(remove_count=500, product=product)
        assert cart.products[product] == 500

    def test_remove_more_then_product(self, product, cart):
        cart.add_product(buy_count=1000, product=product)
        cart.remove_product(remove_count=1500, product=product)
        assert len(cart.products) == 0



    def test_clear(self, product, cart):
        cart.add_product(buy_count=100, product=product)
        cart.clear()
        assert len(cart.products) == 0

    def test_total_price_1(self, product, cart):
        cart.add_product(buy_count=1, product=product)
        assert cart.get_total_price() == 100

    def test_total_price_5(self, product, cart):
        cart.add_product(buy_count=5, product=product)
        assert cart.get_total_price() == 500

    def test_buy(self, product, cart):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            assert cart.buy()
