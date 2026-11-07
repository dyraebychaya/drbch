 def schetchik(func, imya):
    count = [0]

    def obvertka():
        count[0] = count[0] + 1
        print("функция", imya, "вызвана", count[0], "раз")
        return func()

    return obvertka


def privet():
    print("Привет!")


def poka():
    print("Пока!")


privet = schetchik(privet, "privet")
poka = schetchik(poka, "poka")

privet()
poka()

