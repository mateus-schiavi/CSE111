import pytest
import numpy as np
from final_complex import main, repeat

def test_main():
    for _ in range(np.inf):
        main == input()
        
        assert main == True
    

    
pytest.main(["-v", "--tb=line", "-rN", __file__])