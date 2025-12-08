import pytest

from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "big_bun"
    bun.get_price.return_value = 111
    return bun
