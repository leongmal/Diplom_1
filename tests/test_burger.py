from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:
    def test_set_buns(self, mock_bun):
        burg = Burger()
        burg.set_buns(mock_bun)
        assert burg.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burg = Burger()
        burg.add_ingredient(mock_ingredient)
        assert burg.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, mock_ingredient):
        burg = Burger()
        burg.add_ingredient(mock_ingredient)
        burg.remove_ingredient(0)
        assert len(burg.ingredients) == 0
