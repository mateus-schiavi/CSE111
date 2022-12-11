from final_complex import main, repeat
import pytest

def test_main():
   assert input == main()
    
def test_repeat():
    assert answer == repeat()
    
pytest.main(["-v", "--tb=line", "-rN", __file__])