from project import Taxpayer
from project import tax
from project import nattax
import pytest


def test_str():
    taxpayer = Taxpayer("name", 0, 0)
    assert str(taxpayer) == "\nDear name,\n\nBetween the tax year of 6 April 2023 to 5 April 2024, your estimated taxed salary is around £0.00.\n"


def test_tax():
    assert tax(12, 20) == 12480
    assert tax(0, 0) == 0
    with pytest.raises(TypeError):
        assert tax("cat", "dog")

def test_nattax():
    assert nattax(12, 20) == 0
    assert nattax(0, 0) == 0
    with pytest.raises(TypeError):
        assert nattax("cat", "dog")

