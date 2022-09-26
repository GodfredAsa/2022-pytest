from before.pay.order import Order, LineItem, OrderStatus


def test_empty_order_total() -> None:
    order = Order()
    assert order.total == 0


def test_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="shoes", price=100))
    assert order.total == 100


# tests the total price of an order with 2 items
def test_order_multi_line_item_total() -> None:
    order = Order()
    order.line_items.append(LineItem(name="shoes", price=100))
    order.line_items.append(LineItem(name="sandals", price=100))
    assert order.total == 200


def test_order_pay() -> None:
    order = Order()
    order.pay()
    assert order.status == OrderStatus.PAID
