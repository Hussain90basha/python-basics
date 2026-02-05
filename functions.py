def func_name():
    print("Hello")

print(func_name())    

def mult(a, b, *args, **kwargs):
    # *args -> pass any no: of position arguments
    # **kwargs -> pass any no: keyword arguments
    print(a, b, args, kwargs)
    return a * b  # default is none
# a=4, b=5 are keyword arguments, as they contains keys and values
# '3.0', 3 are called as positional arguments
res = mult ('3.0', 3, 4, 5, c=10, d=20)
print(res)