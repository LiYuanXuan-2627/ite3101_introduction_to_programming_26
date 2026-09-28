def cube(number:str):
    return number ** 3

def by_three(number:str):
    if number % 3 ==0:
        return cube(number)
    else:
        return False