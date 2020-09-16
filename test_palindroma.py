import pytest
from palindroma import frasePalindroma

def test_frasePalindroma():
    assert frasePalindroma("oro") == True

@pytest.mark.parametrize(
    "input_a, expected",
    [
        ("reconocer",True),
        ("amor a roma",True),
        ("sometemos", True)
    ]
)
def test_frasePalindroma_multi(input_a, expected):
    assert frasePalindroma(input_a) == expected