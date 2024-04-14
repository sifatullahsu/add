# MTH311
# Interpolation python program

def main():
    x = []
    y = []
    sum = 0
    lf = 0

    n = int(input("Enter number of data: "))
    print("Enter data:")
    for i in range(1, n+1):
        x.append(float(input(f"x[{i}] = ")))
        y.append(float(input(f"y[{i}] = ")))

    xp = float(input("Enter interpolation point: "))

    for i in range(1, n+1):
        lf = 1
        for j in range(1, n+1):
            if j != i:
                lf *= (xp - x[j-1]) / (x[i-1] - x[j-1])
        sum += lf * y[i-1]

    print(f"Interpolating value at point {xp:.4f} is {sum:.4f}.")


main()
