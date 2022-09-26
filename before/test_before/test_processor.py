from before.pay.processor import PaymentProcessor
import pytest

API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"


# GIVEN IN VALID API KEY RAISE VALUE ERROR
def test_invalid_api_key() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(api_key="")
        processor.charge(card="1249190007575069", month=12, year=2024, amount=100)


def test_card_date() -> None:
    processor = PaymentProcessor(api_key=API_KEY)
    processor.charge(card="1249190007575069", month=12, year=2024, amount=100)


# GIVEN INVALID CARD DATE RAISES AN ERROR
def test_card_invalid_date() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(api_key=API_KEY)
        processor.charge(card="1249190007575069", month=12, year=1900, amount=100)


def test_card_number_invalid_luhn():
    payment_processor = PaymentProcessor(api_key=API_KEY)
    assert not payment_processor.luhn_checksum(card_number="1248190007575069")


def test_card_number_valid_luhn():
    payment_processor = PaymentProcessor(api_key=API_KEY)
    assert payment_processor.luhn_checksum(card_number="1249190007575069")


def test_charge_card_valid():
    processor = PaymentProcessor(api_key=API_KEY)
    processor.charge(card="1249190007575069", month=12, year=2024, amount=100)


def test_charge_card_invalid():
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor(api_key=API_KEY)
        payment_processor.charge(card="1249190007575068", month=12, year=2024, amount=100)