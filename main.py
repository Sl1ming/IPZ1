def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Введіть кількість чисел Фібоначчі, які потрібно обчислити
n = int(input("Введіть кількість чисел Фібоначчі: "))

# Виведення результату
fib_numbers = fibonacci(n)
print(f"Перші {n} чисел Фібоначчі: {fib_numbers}")
