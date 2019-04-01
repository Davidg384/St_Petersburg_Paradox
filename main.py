# Buffon's experiment v2, CSC edition'

from collections import defaultdict
from math import log
from os import getcwd
from os.path import exists, join
from random import choice

import matplotlib.pyplot as plt


def petersburg():
    h_t = [0, 1]
    count = 0
    flip = ''
    while flip != 0:
        flip = choice(h_t)
        count += 1
    return 2 ** count


def buffon():
    return [petersburg() for i in range(2048)]


def trials():
    trials = [1000, 2048, 5000, 10000, 50000, 100000, 500000, 1000000]
    avg_payouts = []
    for trial in trials:
        _sum = 0
        for i in range(trial):
            payout = petersburg()
            _sum += payout
        avg_payouts.append(_sum / trial)

    plt.bar(range(len(trials)), avg_payouts, linewidth=2.0)
    plt.show()


def buffon_trials():

    if exists(join(getcwd(), 'averages.txt')):
        with open(join(getcwd(), 'averages.txt'), 'r') as fileobj:
            avg_payouts = [int(x.strip('\n')) for x in fileobj.readlines()]
        count_dict = defaultdict(int)
        for avg in avg_payouts:
            count_dict[avg] += 1
        # print(avg_payouts)
    else:
        avg_payouts = []
        count_dict = defaultdict(int)
        for i in range(1000000):
            avg = sum(buffon()) // 2048
            avg_payouts.append(avg)
            count_dict[avg] += 1
        with open(join(getcwd(), 'averages.txt'), 'w') as fileobj:
            for avg in avg_payouts:
                fileobj.write('{}\n'.format(avg))


    _max = 400
    frequencies = []
    for i in range(_max):
        frequency = count_dict[i]
        if frequency!=0:
            frequencies.append(log(count_dict[i], 2))
        else:
            frequencies.append(0)

    plt.bar(range(_max), frequencies, linewidth=0.01)
    plt.show()


def main():
    # trials()
    buffon_trials()


main()
