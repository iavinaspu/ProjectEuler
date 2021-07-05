def fib(num):
    a = 1
    b = 2
    sum = b
    while(b<=num):
        temp = a
        a = b
        b = temp + b
        if(b%2==0):
            sum +=b

    return sum


print(fib(4000000))
