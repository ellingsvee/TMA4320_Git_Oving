"""
Enkel kalkulator for TMA4320
"""

def addere(a, b):
    """Legger sammen to tall"""
    return a + b

def subtrahere(a, b):
    """Trekker b fra a"""
    return a - b

def dividere(a, b):
    """Deler a på b"""
    if b == 0:
        return "Kan ikke dele på null!"
    return a / b

# Test funksjonene
if __name__ == "__main__":
    print("5 + 3 =", addere(5, 3))
    print("5 - 3 =", subtrahere(5, 3))
    print("6 / 2 =", dividere(6, 2))

def multipliser(a, b):
    return a * b