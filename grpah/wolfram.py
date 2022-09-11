from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr

if __name__ == "__main__":
    session = WolframLanguageSession()
    resuilt = session.evaluate(wlexpr('Range[5]'))
    print(resuilt)
    resuilt = session.evaluate(wlexpr('f[x_] = 2 * x'))
    print(resuilt)
    resuilt = session.evaluate(wlexpr('D[f[x], x]'))
    print(resuilt)
    session.stop()
