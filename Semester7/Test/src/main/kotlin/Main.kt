import java.nio.file.Paths

fun main(args: Array<String>) {
    println(Paths.get(".").toAbsolutePath())

    val a: Int = 1
    val b: Short = 2
    val c: Byte = 3
    val d: Long = 4
    val e: Double = 5.5
    val f: Float = 6.6f
    val x: String = "x";

    val numbA = RNumber(a)
    val numbB = RNumber(b)
    val numbC = RNumber(c)
    val numbD = RNumber(d)
    val numbE = RNumber(e)
    val numbF = RNumber(f)
    val varX = RVariable(x);

    println("a = $numbA")
    println("b = $numbB")
    println("c = $numbC")
    println("d = $numbD")
    println("e = $numbE")
    println("f = $numbF")
    println("x = $varX")

    val aPb = RAdd(numbA, numbB)
    println("a + b = $aPb")

    val cPdPe = RAdd(RAdd(numbC, numbD), numbE)
    println(cPdPe)

    val expr = FunctionPattern("TestClass", "double", "func", "double a, double x, double y", "a * x + y")
    println(expr)

    val compiler = CodeCompiler()
    val cls = compiler.compile(expr)
    println(cls.invoke(1, 2, 3))

    val equation = RAdd(numbC, varX)
    println(equation)
}

interface RExpression

class RNumber(private val value: Number): RExpression {
    override fun toString(): String {
        return value.toString()
    }
}

class RVariable(private val name: String): RExpression {
    override fun toString(): String {
        return name;
    }
}

class RAdd(private val left: RExpression, private val right: RExpression): RExpression {
    override fun toString(): String {
        return "$left + $right"
    }
}
