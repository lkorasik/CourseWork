from collections import Counter


def regime_map(x_start, a_range, b_range, time_range, f, file_path):
    result = dict()
    for a in a_range:
        fk = round(a, 3)
        result[fk] = dict()
        print(fk)
        for b in b_range:
            sc = round(b, 3)
            result[fk][sc] = []
            x0 = x_start
            for _ in time_range:
                xt = f(a, b, x0)
                x0 = xt
            for t in range(20):
                xt = f(a, b, x0)
                result[fk][sc].append(xt)
                x0 = xt

    print("data collected")

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

                # используй set
                di = Counter(data)
                # print(fk, sc, Counter(data))
                # можно забить на это условие?
                if len(di.keys()) == j:
                    res[j].append([fk, sc, di.keys()])
                    continue

    for j in res.keys():
        for i in res[j]:
            print(i[0], i[1], set(i[2]))

    peq = open(file_path + "eqX2Gt2X1.txt", "w")
    peq1 = open(file_path + "eqX2Lt2X1.txt", 'w')
    c2 = open(file_path + 'cycle2.txt', 'w')
    c3 = open(file_path + 'cycle3.txt', 'w')
    c4 = open(file_path + 'cycle4.txt', 'w')
    c5 = open(file_path + 'cycle5.txt', 'w')
    c6 = open(file_path + 'cycle6.txt', 'w')
    c7 = open(file_path + 'cycle7.txt', 'w')
    c8 = open(file_path + 'cycle8.txt', 'w')
    c9 = open(file_path + 'cycle9.txt', 'w')
    c11 = open(file_path + 'cycle11.txt', 'w')
    c10 = open(file_path + 'cycle10.txt', 'w')
    c12 = open(file_path + 'cycle12.txt', 'w')
    c13 = open(file_path + 'cycle13.txt', 'w')
    c14 = open(file_path + 'cycle14.txt', 'w')
    c15 = open(file_path + 'cycle15.txt', 'w')

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

    peq1.close()
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
