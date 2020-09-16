import pytest
from poblacion import poblacionmayor

def test_poblacion():
    assert poblacionmayor(35,19.9,2019) == 2077

@pytest.mark.parametrize(
    "paisA, paisB,año, expected",
    [
        (45.9,13,2025,2155),
        (23,15,2001,2045),
        (10,2,2020,2185),
    ]
)
def test_poblacion_multi(paisA, paisB,año, expected):
    assert poblacionmayor(paisA, paisB,año) == expected