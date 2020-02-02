def fibo(n, memo):
    if n in memo:
        return memo[n]

    if n <= 2:
        f = n
    else:
        f = fibo(n-1, memo) + fibo(n-2, memo)

    memo[n] = f
    return memo
