#pytest file should start with test_ or ends with _test
#pytest method names start with test
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello team")


def test_secondgreetCreditcard():
    print("Good Morning")

@pytest.fixture()
def setup():
    print("execute first")
    yield
    print("i will execute last")

def test_fixtureDemo(setup):
    print("execute steps in fixture demo method")
