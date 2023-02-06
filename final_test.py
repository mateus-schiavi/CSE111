import pytest
from final_complex import perform_operation

def test_perform_operation():
    assert perform_operation(1, 2, 3, 4, "sum") == (4 + 6j)
    assert perform_operation(1, 2, 3, 4, "minus") == (-2 - 2j)
    assert perform_operation(1, 2, 3, 4, "times") == (-5 + 10j)
    assert perform_operation(1, 2, 3, 4, "division") == (0.44 + 0.08j)
    with pytest.raises(ZeroDivisionError):
        perform_operation(1, 2, 0, 0, "division")
    with pytest.raises(AttributeError):
        perform_operation(1, 2, 3, 4, "invalid")

    
pytest.main(["-v", "--tb=line", "-rN", __file__])