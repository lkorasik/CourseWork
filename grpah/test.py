from julia import Main


if __name__ == "__main__":
    Main.include("test.jl")
    print(Main.Test.f(3))
