import pytest

from pages.potfolio import portfolio_cls


@pytest.mark.smoke

def test_portfolio(page):
    portfolio_obj=portfolio_cls(page)