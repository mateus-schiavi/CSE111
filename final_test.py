import pytest
from final_complex import main, repeat

def test_main():
    result = main()
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    
def test_repeat():
    result = repeat("Hello", 3)
    assert result == "HelloHelloHello", f"Expected 'HelloHelloHello', but got {result}"


    

    
pytest.main(["-v", "--tb=line", "-rN", __file__])