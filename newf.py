def outer():

    funcs = []

    for i in range(3):
             def inner(i=i):
                 return i * 2
                 
             funcs.append(inner)

    return funcs

a, b, c = outer()

print(a(), b(), c())