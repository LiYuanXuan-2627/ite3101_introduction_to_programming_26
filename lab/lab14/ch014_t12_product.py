def product(sequence):
    """Return the product of all the numbers in sequence."""
    result = 1
    for number in sequence:
        result *= number
    return result