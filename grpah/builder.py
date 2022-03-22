class Builder:
    @staticmethod
    def stable(a, x12, b_range, precision, function, dfunction, d):
        # Нижняя, т.е. \bar{x}_1
        root = []
        draw_x1 = []
        draw_y1 = []
        x = x12 - (x12 / 4)
        for b in b_range:
            x = Builder.single_newton(a, b, x, precision, function, dfunction)
            root.append(x)
            draw_x1.append(b)
            draw_y1.append(d(a, b, x))  # Значения производной

        result = [[draw_x1, draw_y1]]

        # Верхняя, т.е. \bar{x}_2
        root = []
        draw_x2 = []
        draw_y2 = []
        x = x12 + (x12 / 4)
        for b in b_range:
            x = Builder.single_newton(a, b, x, precision, function, dfunction)
            root.append(x)
            draw_x2.append(b)
            draw_y2.append(d(a, b, x))

        result.append([draw_x2, draw_y2])

        # Верхняя, т.е. x_0
        root = []
        draw_x3 = []
        draw_y3 = []
        x = 0
        for b in b_range:
            x = Builder.single_newton(a, b, x, precision, function, dfunction)
            root.append(x)
            draw_x3.append(b)
            draw_y3.append(d(a, b, x))

        result.append([draw_x3, draw_y3])

        draw_x4 = []
        draw_y4 = []
        for b in b_range:
            draw_x4.append(b)
            draw_y4.append(1)

        result.append([draw_x4, draw_y4])

        draw_x4 = []
        draw_y4 = []
        for b in b_range:
            draw_x4.append(b)
            draw_y4.append(-1)

        result.append([draw_x4, draw_y4])

        return result
