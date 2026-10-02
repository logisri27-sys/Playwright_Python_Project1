import pytest

from pages.devlopment import devlopment_cls

@pytest.mark.smoke

def test_dev(page):
    test_dev_obj=devlopment_cls(page)
    # test_dev_obj.web_Dev()
    # test_dev_obj.ui_ux()
    # test_dev_obj.app_Dev()
    # test_dev_obj.graphic_design()
    # test_dev_obj.social_media()
    test_dev_obj.socialmediapageclick()
