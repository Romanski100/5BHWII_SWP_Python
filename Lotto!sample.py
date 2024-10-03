import random


def lotto_ziehung():
    zahlen = list(range(1, 46))
    gezogen = []

    for _ in range(6):
        idx = random.randint(0, len(zahlen) - 1)
        gezogen.append(zahlen[idx])

        zahlen[idx], zahlen[-1] = zahlen[-1], zahlen[idx]
        zahlen.pop()

    gezogen.sort()
    return gezogen


def lotto_statistik():
    statistik = {i: 0 for i in range(1, 46)}

    for _ in range(1000):
        ziehung = lotto_ziehung()
        for zahl in ziehung:
            statistik[zahl] += 1  

    return statistik


def main():

    print("Einmal ziehen:")
    einmalige_ziehung = lotto_ziehung()
    print("Gezogene Zahlen:", einmalige_ziehung)


    print("\nStatistik nach 1000 mal ziehen:")
    statistik = lotto_statistik()


    for zahl, haeufigkeit in sorted(statistik.items()):
        print(f"Zahl {zahl}: {haeufigkeit} Mal gezogen")


if __name__ == "__main__":
    main()
