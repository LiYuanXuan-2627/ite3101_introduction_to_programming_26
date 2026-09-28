def cube(number:str):
    return number * number

def by_three(number:str):
    if number % 3 ==0:
        return cube(number)