def biggest_number(*args):
    print(max(args))
    return max(args)


def smallest_number(*args):
    print(min(args))
    return min(args)


def distance_from_zero(arg):
    print(abs(arg))
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
#it will print the biggest number, smallest number and distance from zero of the given numbers