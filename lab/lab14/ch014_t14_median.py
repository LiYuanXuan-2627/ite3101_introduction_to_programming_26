def median(numbers):
    """
    Calculate the median of a list of numbers.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    float: The median value.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 1:
        # If odd, return the middle element
        return sorted_numbers[n // 2]
    else:
        # If even, return the average of the two middle elements
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2