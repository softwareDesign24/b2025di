# import pytest
from circulatory_system import Heart

# Starting tests...
def test_01():
    a = Heart(60)
    """ Check that check_health() == True """
    assert a.check_health() == True

def test_02():
    a = Heart(200)
    """ Check that check_health() == False """
    assert a.check_health() == False
