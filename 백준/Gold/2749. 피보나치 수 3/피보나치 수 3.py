import sys
input = sys.stdin.readline

def matrix_mult(A, B, mod=1000000):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]
def matrix_power(matrix, power, mod=1000000):
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = matrix
    while power:
        if power % 2 == 1:
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod)
        power //= 2
    return result
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    F = [[1, 1], [1, 0]]
    result = matrix_power(F, n - 1)
    return result[0][0]
n = int(input())
print(fibo(n))