import pytest
from final_complex import main, repeat

def test_main():
    assert test_main() == True
    

    
pytest.main(["-v", "--tb=line", "-rN", __file__])