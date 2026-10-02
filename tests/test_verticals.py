import pytest

from pages.Verticals import vertical_cls

@pytest.mark.smoke
def test_page(page):
   trank = vertical_cls(page)
   #trank.Clicking_trading_options()
   # trank.Retail_options()
   # trank.heathcare_options()
   # trank.fintech_options()
   trank.get_free_demo()




