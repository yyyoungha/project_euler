def sum_of_squares(n):
    return n * (n + 1) * (2*n + 1) // 6

def square_of_sum(n):
    a = n * (n + 1) // 2
    return a * a;

n = 100
print(square_of_sum(n) - sum_of_squares(n))
