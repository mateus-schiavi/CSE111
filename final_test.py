import pytest
from final_complex import main, repeat

def test_main():
    assert main(input) == True
    
def test_repeat():
    assert repeat(main) == True
    
pytest.main(["-v", "--tb=line", "-rN", __file__])