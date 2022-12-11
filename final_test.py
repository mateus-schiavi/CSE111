from final_complex import main, repeat
import pytest

def test_main():
   assert input() == 1
    
def test_repeat():
    assert repeat == 0
    
pytest.main(["-v", "--tb=line", "-rN", __file__])