from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
        if browser=='chrome':
           driver = webdriver.Chrome(executable_path='Driver/chromedriver/chromedriver')
           print("launching chrome browser")
        elif browser=='firefox':
           driver = webdriver.Firefox(executable_path='Driver/geckodriver/geckodriver')
           print("launching firefox browser")
        return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser",default="chrome")

### Pytest HTML Report #####
def pytest_configure(config):
        config._metadata['Project Name'] = 'Director Portal'
        config._metadata['Module Name'] = 'Login'
        config._metadata['Tester'] = 'TicvicQA'









