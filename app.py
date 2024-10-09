print("Hello world")

def funcao_de_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return funcao_de_fibonacci(n-1) + funcao_de_fibonacci(n-2)

print(funcao_de_fibonacci(10))

fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))

