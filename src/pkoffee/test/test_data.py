import pytest
import pandas as pd
from pkoffee.data import validate, MissingColumnsError

def test_validate_success():
    df = pd.DataFrame({
        'cups': [1, 2, 3],
        'productivity': [4.5, 5.5, 6.5]
    })
    
    assert validate(df) is None

def test_validate_missing_columns():
    df = pd.DataFrame({'cups': [1, 2, 3]}) 
    
    with pytest.raises(MissingColumnsError) as excinfo:
        validate(df)
    
    assert 'productivity' in str(excinfo.value)



def test_validate_invalid_types():
    from pkoffee.data import validate, ColumnTypeError 
    invalid_data = pd.DataFrame({'cups': ['x', 'y', 'z'], 'productivity': [1, 2, 3]})
    with pytest.raises(ColumnTypeError):
        validate(invalid_data)



def test_validate_empty_dataframe():
    df = pd.DataFrame({'cups': pd.Series(dtype='float64'), 'productivity': pd.Series(dtype='int64')})
    assert validate(df) is None
