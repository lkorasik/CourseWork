def lyapunov(epsilon, b_range, x_0, time_range, T, f, lambda_):
    dxs = []
    bs = []

    for b in b_range:
        x0 = x_0
        summary = 0
        for _ in time_range:
            x0d = x0 + epsilon
            x0 = f(b, x0)
            x0d = f(b, x0d)
            summary += lambda_(abs(x0d - x0), epsilon)
        dxs.append(summary / T)
        bs.append(b)

    return bs, dxs
