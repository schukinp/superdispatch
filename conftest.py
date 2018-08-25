import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(60)
    selenium.set_page_load_timeout(60)
    return selenium

@pytest.fixture
def chrome_options():
    chrome_options = Options()
  # chrome_options.add_argument('--headless')
  # chrome_options.add_argument('--disable-gpu')
  # chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('----start-maximized')
    return chrome_options