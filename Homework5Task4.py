a = int(input('Введите длину списка: '))
def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fibo(a)))