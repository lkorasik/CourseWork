from julia import Main


if __name__ == "__main__":
    print("HW")
    print(Main.eval('A = rand(3, 3)'))
    Main.eval('include(\"test.jl\")')
    print(Main.eval('Test.f(3)'))
    print(Main.Test.f(3))
