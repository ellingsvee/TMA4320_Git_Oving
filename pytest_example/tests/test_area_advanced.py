import numpy as np
import pytest
from area import circle_area

#############################################################################
# En mer avansert med bruk av fixtures. Lettere å teste flere kombinasjoner
#############################################################################

DTYPE = [
    pytest.param("float64", id="float64"),
    pytest.param("complex128", id="complex128"),
]

ARRAY_SHAPE = [
    pytest.param((1,), id="1D"),
    pytest.param((5, 5), id="2D-5x5"),
]


@pytest.fixture(params=DTYPE, autouse=True)
def dtype(request: pytest.FixtureRequest) -> str:
    return request.param


@pytest.fixture(params=ARRAY_SHAPE, autouse=True)
def array_shape(request: pytest.FixtureRequest) -> tuple:
    return request.param

def test_circle_area_advanced(
    dtype: str,
    array_shape: tuple,
):
    """Area of circle should be pi * r^2."""

    # Generate a random radius array
    radius = np.random.rand(*array_shape).astype(dtype) * 10

    # Comupte true area
    true_circle_area = np.pi * radius**2

    # Test if the function works correctly
    assert np.allclose(circle_area(radius), true_circle_area), (
        f"circle_area failed for dtype={dtype} and shape={array_shape}"
    )
