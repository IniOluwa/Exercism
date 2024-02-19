"""
Calculating Amount of Grains on a Chess Board
Squaring The Number on Every Square
"""

# Square Values
def square(number):
    """Check Return Number of Grains on Square"""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    # Populate Grains
    grains = [1]
    while len(grains) < 64:
        grains.append(grains[-1] * 2)

    # Return Number of Grains on Specific Square
    return grains[number - 1]

# Get Total Grains
def total():
    """Return Total Grains Number"""
    return sum([square(x) for x in range(1, 65)])
