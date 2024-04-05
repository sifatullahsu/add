def f(x, y):
    return (y*y - x*x) / (y*y + x*x)


def runge_kutta(x0, y0, xn, n):
    h = (xn - x0) / n
    print("\nx0\ty0\tyn")
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)

        k = (k1 + 2*k2 + 2*k3 + k4) / 6
        yn = y0 + k

        print("%0.4f\t%0.4f\t%0.4f" % (x0, y0, yn))

        x0 += h
        y0 = yn

    return yn


# Example usage
x0 = float(input("Enter Initial Condition\nx0 = "))
y0 = float(input("yo= "))
xn = float(input("Enter calculation point xn = "))
n = int(input("Enter number of steps: "))

result = runge_kutta(x0, y0, xn, n)
print("\nValue of y at x =", xn, "is", result)
