def fl(x, y, z):
    return (17 - y + 2 * x) / 20


def f2(x, y, z):
    return (18 - 3 * x + 2) / 20


def f3(x, y, z):
    return (25 - 2 * x + 3 * y) / 20


def jacobi(x0, y0, z0, e):
    count = 1
    print("Count\tx\ty\tz")
    while True:
        x1 = fl(x0, y0, z0)
        y1 = f2(x0, y0, z0)
        z1 = f3(x0, y0, z0)
        print(f"{count}\t{x1:.4f}\t{y1:.4f}\t{z1:.4f}")

        el = abs(x0 - x1)
        e2 = abs(y0 - y1)
        e3 = abs(z0 - z1)

        if el <= e and e2 <= e and e3 <= e:
            break

        count += 1

        x0 = x1
        y0 = y1
        z0 = z1

    print(f"\nSolution: x = {x1:.4f}, y = {y1:.4f}, and z = {z1:.4f}")


# Example usage
x0 = float(input("Enter initial guess for x: "))
y0 = float(input("Enter initial guess for y: "))
z0 = float(input("Enter initial guess for z: "))
e = float(input("Enter tolerable error: "))

jacobi(x0, y0, z0, e)
