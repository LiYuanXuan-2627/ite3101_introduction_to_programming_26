n = [3, 5, 7]

def double_list(x):
    new_list = []
    for i in range(0, len(x)):
        new_list.append(x[i] * 2)
    return x

# Don't forget to return your new list!

print(double_list(n))
