def taylor(iks, eps):
    f = []
    for i in range(1, len(iks)):
        a = 1
        summa = a
        z = -iks[i]**2/4
        for n in range(0, 10000):
            a = a*z/(n+1)**2
            summa = summa + a
            if abs(a) < eps:
                break
        f[i] = summa
    return f

