for k in range(10):
    for p in range(10):
        for f in range(10):
            for u in range(10):
                if (k+p+f+u) ** 4 + 24 == 1000 * k + 100 * p + 10 * f + u:
                    print(1000 * k + 100 * p + 10 * f + u)

