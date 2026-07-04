# Create a recursive function to calculate the sum of the first n natural numbers

def sum_n(n):
     if n == 1:
        return 1
     return (n + sum_n(n - 1))

x = sum_n(1)

print(x)
