import pytest


@pytest.fixture(scope="class")
def setup():
    print("execute first")
    yield
    print("i will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is created")
    return ["name","password","facebook.com"]

@pytest.fixture(params=["chrome","Firefox", "IE"])
def crossBrowser(request):
    return request.param
