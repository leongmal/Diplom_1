from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:
    def test_set_buns(self, mock_bun):
        burg = Burger()
        burg.set_buns(mock_bun)
        assert burg.bun == mock_bun
