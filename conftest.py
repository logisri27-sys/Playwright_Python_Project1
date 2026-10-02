from pathlib import Path

import pytest
import pytest_html
from playwright.sync_api import sync_playwright

from config import BASE_URL

VIDEOS_DIR = Path("videos")
SCREENSHOTS_DIR = Path("screenshots")


@pytest.fixture
def page(request):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    VIDEOS_DIR.mkdir(exist_ok=True)

    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(VIDEOS_DIR),
        record_video_size={"width": 1280, "height": 720},
    )
    page = context.new_page()

    page.goto(BASE_URL)
    page.wait_for_load_state("load")

    yield page

    try:
        context.close()
        request.node._video_path = page.video.path() if page.video else None
    finally:
        browser.close()
        p.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = list(getattr(report, "extra", []))

    video_path = getattr(item, "_video_path", None)

    if report.when == "teardown" and video_path:
        video_file = Path(video_path)
        if video_file.exists():
            extra.append(
                pytest_html.extras.html(
                    f'<video controls width="640"><source src="{video_file.as_uri()}" type="video/webm"></video>'
                )
            )

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            SCREENSHOTS_DIR.mkdir(exist_ok=True)
            file_name = SCREENSHOTS_DIR / f"{item.name}.png"
            page.screenshot(path=str(file_name))
            extra.append(pytest_html.extras.image(str(file_name)))

    report.extra = extra
    report.extras = extra
