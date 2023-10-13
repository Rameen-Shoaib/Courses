import pytest
from project import exchange_rate, convert, currency_name, get_currencies, print_currencies


def test_currency_name():
    with pytest.raises(TypeError):
        currency_name("pkr")


def test_exchange_rate():
    assert exchange_rate("USD", "PKR") == 283.478124
    assert exchange_rate("USD", "XOF") == 598.483424
    assert exchange_rate("ZWL", "OMR") == 0.001196


def test_convert():
    assert convert("USD", "PKR", 100) == 28347.8124
    assert convert("LVL", "MAD", 1000) == 16739.412
