import pytest

@pytest.mark.skip
def test_firstProgram2():
    msg = "Hello"
    assert msg == "Hi", "Test failed"


@pytest.mark.smoke
@pytest.mark.xfail
def test_secondCreditcard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition does not match"


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
