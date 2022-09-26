# THIS IS THE FIRST TEST WRITTEN BY ME
# LINE ITEM IS IN THE ORDER.PY FILE
from before.pay.order import LineItem


# test default total without qty set
def test_line_item_default() -> None:
    line_item = LineItem(name="shoes", price=100)
    assert line_item.total == 100


# tests total with qty set
def test_line_item_qty() -> None:
    line_item = LineItem(name="shoes", price=100, quantity=2)
    assert line_item.total == 200
