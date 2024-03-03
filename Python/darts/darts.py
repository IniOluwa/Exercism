# Calculate Dart Game Score Based on Coordinates
def score(x, y):
    # Get Radii and Calculate Points
    r_inner, r_middle, r_outer = 1, 5, 10
    xy_coordinates = x**2 + y**2
    if xy_coordinates - r_inner**2 <= 0:
        return 10
    if xy_coordinates - r_middle**2 <= 0:
        return 5
    if xy_coordinates - r_outer**2 <= 0:
        return 1
    return 0
