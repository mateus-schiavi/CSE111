import pytest
from final_complex import main, repeat

def test_main():
   assert main() == 1
    
def test_repeat():
    assert repeat == 0
    
pytest.main(["-v", "--tb=line", "-rN", __file__])