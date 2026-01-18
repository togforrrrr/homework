#3
def powers_of_three(max_degree):
    i = 0
    while i <= max_degree:
        yield 3 ** i
        i += 1


for value in powers_of_three(10):
    print(value)
