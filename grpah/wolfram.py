from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr, wl

if __name__ == "__main__":
    with WolframLanguageSession() as session:

        result = session.evaluate(wlexpr('Range[5]'))
        print(result)

        result = session.evaluate('Range[5]')
        print(result)

        result = session.evaluate(wl.Range(5))
        print(result)

        result = wl.BarChart([1, 2, 3])
        expr = wl.Export("C:/users/lkora/Desktop/t.png", result, 'PNG')
        session.evaluate(expr)

        result = session.evaluate("f[x_] := 2 * x")
        print(session.evaluate('f[2]'))

        result = wlexpr('f[x_] := 3 * x')
        session.evaluate(result)
        result = session.function(wlexpr('f'))
        print(result(3))

        future = session.evaluate_future('Pause[3]; 1 + 1')
        print(future.result())
