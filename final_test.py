import pytest
from final_complex import main, repeat

def test_main():
   return main()
    
def test_repeat():
    return repeat()
    
pytest.main(["-v", "--tb=line", "-rN", __file__])