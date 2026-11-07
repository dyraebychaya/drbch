def fibonachi(n):
    a = 0
    b = 1
    spisok = []
    for i in range(n):
        spisok.append(a)
        a, b = b, a + b
    return spisok

print(fibonachi(10))