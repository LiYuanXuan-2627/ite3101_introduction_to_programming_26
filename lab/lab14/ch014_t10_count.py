def count(sequence, item):
    """Count the number of occurrences of item in sequence."""
    count = 0
    for element in sequence:
        if element == item:
            count += 1
    return count