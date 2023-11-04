import pytest

@pytest.mark.add()
def test_add():
    assert 1 + 1 == 2
    
@pytest.mark.sub()
def test_subtract():
    assert 1 - 1 == 0
