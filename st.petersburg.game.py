import random


def coin_flip():
    return random.choice(["heads", "tails"])


def st_pertersburg():
    n = 1
    while coin_flip() == "tails":
        n += 1
    return 2**n


def main():
    expected_value = []
    for n in [1000, 2048, 5000, 10000, 500000, 1000000]:
        winnings = 0
        for games in range(n):
            winnings += st_pertersburg()
        expected_value.append(winnings/n)
    print(expected_value)


main()
