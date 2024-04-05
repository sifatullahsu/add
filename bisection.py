import math


def f(x):
    return math.cos(x) - x * math.exp(x)


def bisection(x0, x1, e):
    step = 1
    fo = f(x0)
    f1 = f(x1)

    # Checking whether given guesses bracket the root or not
    if fo * f1 > 0:
        print("Incorrect Initial Guesses.")
        return None

    print("\nstep\t\tx0\t\t\t\tx1\t\t\t\tx2\t\t\t\tf(x2)")
    while True:
        x2 = (x0 + x1) / 2
        f2 = f(x2)

        print(f"{step}\t\t{x0}\t\t{x1}\t\t{x2}\t\t{f2}")

        if fo * f2 < 0:
            x1 = x2
        else:
            x0 = x2

        if abs(f2) < e:
            break

        step += 1

    print("\nRoot is:", x2)
    return x2


# Example usage
x0 = float(input("Enter first initial guess: "))
x1 = float(input("Enter second initial guess: "))
e = float(input("Enter tolerable error: "))

bisection(x0, x1, e)
