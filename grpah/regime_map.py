import collections
from collections import Counter

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

from builder import Builder
from functions import Functions


def single_newton(a, b, x_start, precision, function, dfunction):
    """Найти один корень с помощью метода Ньютона"""
    x_0 = x_start
    iterations = 0
    while iterations < 10 ** 4:
        x_n = x_0 - function(a, b, x_0) / dfunction(a, b, x_0)
        if np.isnan(x_n):
            break
        if abs(x_n - x_0) < precision:
            break
        x_0 = x_n

        iterations += 1
    res = x_0
    return res


def find_all_roots(x_range, a_range, b_range, precision):
    result = dict()
    for a in a_range:
        result[a] = dict()
        for b in b_range:
            result[a][b] = []

    for a in a_range:
        print(a)
        for b in b_range:
            for x in x_range:
                res = single_newton(
                    a=a,
                    b=b,
                    x_start=x,
                    precision=precision,
                    function=Functions.h,
                    dfunction=Functions.dh)
                result[a][b].append(res)

    for a in a_range:
        for b in b_range:
            for i in range(len(result[a][b])):
                result[a][b][i] = round(result[a][b][i], 3)

    for a in a_range:
        for b in b_range:
            print(Counter(result[a][b]))



def build_regime_map(x_start, a_range, b_range, time_range, f):
    result = dict()
    newtoon = dict()
    for a in a_range:
        fk = round(a, 3)
        result[fk] = dict()
        newtoon[fk] = dict()
        print(fk)
        for b in b_range:
            sc = round(b, 3)
            result[fk][sc] = []
            x0 = x_start
            for t in time_range:
                xt = f(a, b, x0)
                x0 = xt
            # for t in time_range:
            for t in range(20):
                xt = f(a, b, x0)
                result[fk][sc].append(xt)
                x0 = xt

    print("data collected")
    fig, ax = plt.subplots()

    res = dict()
    for j in range(1, 10 + 1):
        res[j] = []
        for a in a_range:
            fk = round(a, 3)
            for b in b_range:
                sc = round(b, 3)
                data = result[fk][sc]
                for i in range(len(data)):
                    data[i] = round(data[i], 3)

                di = Counter(data)
                # print(fk, sc, Counter(data))
                if len(di.keys()) == j:
                    res[j].append([fk, sc, di.keys()])
                    continue

    for j in res.keys():
        for i in res[j]:
            print(i[0], i[1], set(i[2]))

    peq = open("C:\\Users\\lkora\\Desktop\\data\\eqX2Gt2X1.txt", 'w')
    peq1 = open("C:\\Users\\lkora\\Desktop\\data\\eqX2Lt2X1.txt", 'w')
    c2 = open('C:\\Users\\lkora\\Desktop\\data\\cycle2.txt', 'w')
    c3 = open('C:\\Users\\lkora\\Desktop\\data\\cycle3.txt', 'w')
    c4 = open('C:\\Users\\lkora\\Desktop\\data\\cycle4.txt', 'w')
    c5 = open('C:\\Users\\lkora\\Desktop\\data\\cycle5.txt', 'w')
    c6 = open('C:\\Users\\lkora\\Desktop\\data\\cycle6.txt', 'w')
    c7 = open('C:\\Users\\lkora\\Desktop\\data\\cycle7.txt', 'w')
    c8 = open('C:\\Users\\lkora\\Desktop\\data\\cycle8.txt', 'w')
    c9 = open('C:\\Users\\lkora\\Desktop\\data\\cycle9.txt', 'w')
    c11 = open('C:\\Users\\lkora\\Desktop\\data\\cycle11.txt', 'w')
    c10 = open('C:\\Users\\lkora\\Desktop\\data\\cycle10.txt', 'w')
    c12 = open('C:\\Users\\lkora\\Desktop\\data\\cycle12.txt', 'w')
    c13 = open('C:\\Users\\lkora\\Desktop\\data\\cycle13.txt', 'w')
    c14 = open('C:\\Users\\lkora\\Desktop\\data\\cycle14.txt', 'w')
    c15 = open('C:\\Users\\lkora\\Desktop\\data\\cycle15.txt', 'w')

    for j in range(1, 10 + 1):
        line = ""
        k = ""
        for item in res[j]:
            a = item[0]
            b = item[1]

            if j == 1:
                if list(item[2]) == [0.0]:
                    k += str(a) + " " + str(b) + "\n"
                else:
                    line += str(a) + " " + str(b) + "\n"
            else:
                line += str(a) + " " + str(b) + "\n"

        if j == 1:
            peq1.write(k)
            peq.write(line)
        if j == 2:
            c2.write(line)
        if j == 3:
            c3.write(line)
        if j == 4:
            c4.write(line)
        if j == 5:
            c5.write(line)
        if j == 6:
            c6.write(line)
        if j == 7:
            c7.write(line)
        if j == 8:
            c8.write(line)
        if j == 9:
            c9.write(line)
        if j == 10:
            c10.write(line)
        if j == 11:
            c11.write(line)
        if j == 12:
            c12.write(line)
        if j == 13:
            c13.write(line)
        if j == 14:
            c14.write(line)
        if j == 15:
            c15.write(line)

    peq.close()
    c2.close()
    c3.close()
    c4.close()
    c5.close()
    c6.close()
    c7.close()
    c8.close()
    c9.close()
    c10.close()
    c11.close()
    c12.close()
    c13.close()
    c14.close()
    c15.close()

    # print("Attractors found")
    # colors = {1: 'red',
    #           2: 'steelblue',
    #           3: 'green',
    #           4: 'lime',
    #           5: 'darkviolet',
    #           6: 'deeppink',
    #           7: 'aqua',
    #           8: 'navy',
    #           9: 'pink',
    #           10: 'brown',
    #           11: 'gold',
    #           12: 'dodgerblue'}
    #
    # colors = {1: [204 / 255, 204 / 255, 204 / 255],
    #           2: [76 / 255, 102 / 255, 0 / 255],
    #           3: [255 / 255, 0 / 255, 0 / 255],
    #           4: [168 / 255, 2 / 255, 168 / 255],
    #           5: [0 / 255, 253 / 255, 255 / 255],
    #           6: [254 / 255, 255 / 255, 0 / 255],
    #           7: [120 / 255, 55 / 255, 219 / 255],
    #           8: [114 / 255, 153 / 255, 0 / 255],
    #           9: [134 / 255, 18 / 255, 252 / 255],
    #           10: [250 / 255, 145 / 255, 145 / 255],
    #           11: [128 / 255, 116 / 255, 98 / 255],
    #           12: [0 / 255, 255 / 255, 0 / 255],
    #           13: [127 / 255, 0 / 255, 128 / 255],
    #           14: [126 / 255, 127 / 255, 247 / 255],
    #           15: [0 / 255, 1 / 255, 255 / 255]}
    #
    # for i in res.keys():
    #     for item in res[i]:
    #         plt.scatter(item[0], item[1], color=colors[i], linewidths=0.01)
    #
    # print("Data plotted")
    # patches = [mpatches.Patch(color=colors[i], label=i) for i in colors.keys()]
    # ax.legend(handles=patches, loc="center left", bbox_to_anchor=(1, 0.5))
    # plt.ylim(0.01, 0.6)
    # plt.xlim(0.01, 2)
    #
    # plt.savefig("C:\\users\\lkora\\desktop\\a.jpg")

    #plt.show()
