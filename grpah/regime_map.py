import math
from collections import Counter

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

from builder import Builder
from functions import Functions


def build_regime_map(x_start, a_range, b_range, time_range, f):
    result = dict()
    newtoon = dict()
    for a in a_range:
        fk = round(a, 3)
        result[fk] = dict()
        newtoon[fk] = dict()
        for b in b_range:
            sc = round(b, 3)
            result[fk][sc] = []
            x0 = x_start
            for t in time_range:
                xt = f(a, b, x0)
                x0 = xt
            #for t in time_range:
            for t in range(20):
                xt = f(a, b, x0)
                result[fk][sc].append(xt)
                x0 = xt

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
                #print(fk, sc, Counter(data))
                if len(di.keys()) == j:
                    res[j].append([fk, sc])
                    continue

    colors = {1: 'red',
              2: 'steelblue',
              3: 'green',
              4: 'lime',
              5: 'darkviolet',
              6: 'deeppink',
              7: 'aqua',
              8: 'navy',
              9: 'pink',
              10: 'brown',
              11: 'gold',
              12: 'dodgerblue'}

    colors = {1: [204 / 255, 204 / 255, 204 / 255],
              2: [76 / 255, 102 / 255, 0 / 255],
              3: [255 / 255, 0 / 255, 0 / 255],
              4: [168 / 255, 2 / 255, 168 / 255],
              5: [0 / 255, 253 / 255, 255 / 255],
              6: [254 / 255, 255 / 255, 0 / 255],
              7: [120 / 255, 55 / 255, 219 / 255],
              8: [114 / 255, 153 / 255, 0 / 255],
              9: [134 / 255, 18 / 255, 252 / 255],
              10: [250 / 255, 145 / 255, 145 / 255],
              11: [128 / 255, 116 / 255, 98 / 255],
              12: [0 / 255, 255 / 255, 0 / 255],
              13:  [127 / 255, 0 / 255, 128 / 255],
              14: [126 / 255, 127 / 255, 247 / 255],
              15: [0 / 255, 1 / 255, 255 / 255]}

    for i in res.keys():
        for item in res[i]:
            plt.scatter(item[0], item[1], color=colors[i], linewidths=0.01)

    patches = [mpatches.Patch(color=colors[i], label=i) for i in colors.keys()]
    ax.legend(handles=patches, loc="center left", bbox_to_anchor=(1, 0.5))

    plt.show()
