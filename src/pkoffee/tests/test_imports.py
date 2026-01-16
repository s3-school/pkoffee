import numpy as np
import pytest

def test_import():
    from pkoffee import metrics


def test_size_mismatch_true():
    from pkoffee.metrics import check_size_match

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    return check_size_match(a, b)

def test_size_mismatch_false():
    from pkoffee.metrics import check_size_match, SizeMismatchError
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6, 8])

    with pytest.raises(expected_exception=SizeMismatchError):
        check_size_match(a, b)

