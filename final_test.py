from final_complex import main, repeat
import pytest

def test_main():
   assert main == True
    
def test_repeat():
    assert repeat == True
    
pytest.main(["-v", "--tb=line", "-rN", __file__])