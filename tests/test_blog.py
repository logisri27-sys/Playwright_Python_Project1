import pytest

from pages.blog import blog_cls


@pytest.mark.smoke

def test_blog(page):
    blog_obj=blog_cls(page)