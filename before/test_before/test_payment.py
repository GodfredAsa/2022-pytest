# Happy Path Testing
# since the program takes input from users while testing does not require the taking
# on inputs we would mock the input session using monkey patch from pytest

from pytest import MonkeyPatch

from before.pay.order import Order, LineItem
from before.pay.payment import pay_order
from before.pay.processor import PaymentProcessor


def test_pay_order(monkeypatch: MonkeyPatch) -> None:
    # user inputs mocked in here
    inputs = ["1249190007575069", "12", "2024"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    # mocking payment processor
    monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
    # creates an order
    order = Order()
    order.line_items.append(LineItem(name="test", price=100))
    pay_order(order)
