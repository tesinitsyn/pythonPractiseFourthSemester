def distance(x1, y1, x2, y2):
    """
    Returns the Euclidean distance between two points in a 2D plane.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        float: The Euclidean distance between the two given points.

    Examples:
        >>> distance(0, 0, 3, 4)
        5.0
        >>> distance(1, 1, 1, 1)
        0.0
        >>> distance(0, 0, 0, 0)
        0.0
        >>> distance(-1, -1, 1, 1)
        2.8284271247461903
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
