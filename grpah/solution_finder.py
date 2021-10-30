import numpy


def g(x, b, a=1):
    return x-(a*x**2)/((b+x)**6)


x_min = 0.08
x_max = 0.14
x_step = 0.01
x_range = numpy.arange(x_min, x_max, x_step)

b_min = 0.4
b_max = 0.6
b_step = 0.01
b_range = numpy.arange(b_min, b_max, b_step)

size = (b_max - b_min)/b_step * (x_max-x_min)/x_step

f = open("C:\\users\\user\\desktop\\res.txt", 'w')

result = []

c = 0
for b in b_range:
    mini_y = 1000
    mini_x = 0
    mini_b = 0

    for x in x_range:
        c+=1
        y = g(x, b)

        print(f"{c}/{size} {c/size}", end="\r")

        if y < mini_y:
            mini_y = y
            mini_x = x
            mini_b = b

    result.append((mini_x, mini_b, mini_y))
    f.write(f"x={mini_x}|b={mini_b}|y={mini_y}\n")
f.close()

result = sorted(result, key=lambda i: i[2], reverse=True)
print(result[0])
print(result[1])
