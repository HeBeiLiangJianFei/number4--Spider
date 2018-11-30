def fib(n):
    a,b,s = 0,1,0

    while s < n:
        a,b = b,a+b
        s += 1
        yield b

# print(fib(5).__next__())
for i in fib(5):
    print(i)












