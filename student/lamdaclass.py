def myfunc(n):
    return lambda a:a*n
my=myfunc(3)
print(my(11))