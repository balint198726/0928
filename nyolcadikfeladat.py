# Írjuk ki a Fibonacci sorozat első 80 elemét
def Fibonacci():
    fib = [0,1]
    i = 2

    while i < 80:
        fib.append(fib[i-1] + fib[i-2])
        i += 1
    print(fib)