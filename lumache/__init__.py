"""
Lumache - Python library for cooks and food lovers.

This module provides some functions to search and retrieve recipes
from a cookbook.
"""

def get_random_ingredients(kind=None):
    """Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: str or None
    :return: List of ingredients.
    :rtype: list[str]
    :raises RuntimeError: If the kind is unknown.
    """
    return ["shells", "gorgonzola", "parsley"]