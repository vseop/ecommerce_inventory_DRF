import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

EXE_PATH = r'./chromedriver'


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Provide a selenium webdriver instance
    """
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(executable_path=EXE_PATH, options=options)
    yield browser
    browser.close()
