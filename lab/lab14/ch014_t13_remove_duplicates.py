def remove_duplicates(lst):
    """
    Remove duplicates from a list while preserving the order of elements.

    Args:
        lst (list): The input list from which duplicates need to be removed.

    Returns:
        list: A new list with duplicates removed, preserving the original order.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result