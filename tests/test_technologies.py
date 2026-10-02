import pytest

from pages.Technologies import Technologies_cls

@pytest.mark.smoke

def test_tech(page):
    test_technology=Technologies_cls(page)
    # test_technology.ecommerce_options()
    # test_technology.Mobile_app_options()
    # test_technology.ai_options()