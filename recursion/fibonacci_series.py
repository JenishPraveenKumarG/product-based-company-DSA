def fibo(n):
    if n <= 1:
        return n
    
    last = fibo(n-1)
    s_last = fibo(n-2)

    return last + s_last

print(fibo(6))

# TC - 2 power n