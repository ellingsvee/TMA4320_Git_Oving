import numpy as np
import pytest
from area import circle_area


##########################################################################################################
# En enkel måte å skrive tester, men kan bli tungvindt bruke pytest.mark.parametrize for større eksempler
##########################################################################################################

@pytest.mark.parametrize(
    "radius",
    [
        0.5,
        2.0,
    ],
)
def test_circle_area_simple(radius):
    """Area of circle should be pi * r^2."""
    our_function = circle_area(radius)
    expected = np.pi * radius**2
    assert our_function == expected, f"circle_area failed for radius = {radius}" # Assert will raise an error if condition is False