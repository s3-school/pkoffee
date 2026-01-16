import pandas as pd

def test_validate() -> None:

    from pkoffee.data import validate
    """Test validate with valide DataFrame."""
    assert validate(pd.DataFrame({"cups": [0], "productivity": [1.2]})) is None

    

# test for the CI 
