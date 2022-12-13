import pytest
from final_complex import main, repeat

def test_main():
    assert main == value()
    
def test_repeat():
    assert repeat == wordchars()
    
pytest.main(["-v", "--tb=line", "-rN", __file__])