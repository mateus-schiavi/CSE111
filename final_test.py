import pytest
from final_complex import main, repeat

def test_main():
    assert main
    
def test_repeat():
    assert repeat


    

    
pytest.main(["-v", "--tb=line", "-rN", __file__])