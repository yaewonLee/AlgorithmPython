while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    sides = sorted([a, b, c])

    a, b, c = sides[0], sides[1], sides[2]

    if a ** 2 + b ** 2 == c ** 2:
        print("right")
    else:
        print("wrong")