from sympy import Symbol

from visual.line import Line


def _x(xa, xb, xc, xd, ya, yb, yc, yd):
    return (xb * xd * (ya - yc) + xa * xd * (yc - yb) + xa * xc * (yb - yd) + xb * xc * (yd - ya)) / \
           (xd * (ya - yb) + xc * (yb - ya) + (xa - xb) * (yc - yd))


def _y(xa, xb, xc, xd, ya, yb, yc, yd):
    return (xd * (ya - yb) * yc + xa * yb * yc - xc * ya * yd - xa * yb * yd + xc * yb * yd +
            xb * ya * (-yc + yd)) / (xd * (ya - yb) +
                                     xc * (-ya + yb) + (xa - xb) * (yc - yd))


def line_intersection(line1: Line, line2: Line):
    x = Symbol("x")
    y = Symbol("y")

    r = []

    for i in range(len(line1.x) - 1):
        for j in range(len(line2.x) - 1):
            print(i, "/", len(line1.x), j, "/", len(line2.x))

            xa = line1.x[i]
            ya = line1.y[i]
            xb = line2.x[j]
            yb = line2.y[j]

            xc = line1.x[i + 1]
            yc = line1.y[i + 1]
            xd = line2.x[j + 1]
            yd = line2.y[j + 1]

            # Тут найди точку пересечения из алгема

            if xb == xa or yb == ya or xd == xc or yd == yc:
                continue

            x_ = _x(xa, xb, xc, xd, ya, yb, yc, yd)
            y_ = _y(xa, xb, xc, xd, ya, yb, yc, yd)

            # Надо еще убедится, что один отрезок рядом с другим

            if min(xa, xb) < x_ < max(xa, xb) and min(xc, xd) < x_ < max(xc, xd):
                r.append((x_, y_))

    return r


def line_intersection_bad(line1: Line, line2: Line):
    y1 = set(line1.y)
    y2 = set(line2.y)

    common_points = y1.intersection(y2)

    indexes1 = [line1.y.index(i) for i in common_points]
    indexes2 = [line2.y.index(i) for i in common_points]

    x1 = [line1.x[i] for i in indexes1]
    y1 = [line1.y[i] for i in indexes1]

    x2 = [line2.x[i] for i in indexes2]
    y2 = [line2.y[i] for i in indexes2]

    # Рассматривай точки

    return x1 + x2, y1 + y2
