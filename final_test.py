import pytest
from final_complex import main, repeat

def test_main():
    if input > 0:
        assert main == True
    else:
        assert main == False
    
def test_repeat():
    if input > 0:
        assert repeat == True
    else:
        assert repeat == False
    
pytest.main(["-v", "--tb=line", "-rN", __file__])