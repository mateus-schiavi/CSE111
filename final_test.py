import pytest
from final_complex import main, repeat

def test_main():
    assert main == 1
    

    
pytest.main(["-v", "--tb=line", "-rN", __file__])