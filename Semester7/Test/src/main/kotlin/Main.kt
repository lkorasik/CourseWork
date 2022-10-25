import java.nio.file.Paths

fun main(args: Array<String>) {
    println(Paths.get(".").toAbsolutePath())

    val a: Int = 1
    val b: Short = 2
    val c: Byte = 3
    val d: Long = 4
    val e: Double = 5.5
    val f: Float = 6.6f

    val numbA = RNumber(a)
    val numbB = RNumber(b)
    val numbC = RNumber(c)
    val numbD = RNumber(d)
    val numbE = RNumber(e)
    val numbF = RNumber(f)

    println("a = $numbA")
    println("b = $numbB")
    println("c = $numbC")
    println("d = $numbD")
    println("e = $numbE")
    println("f = $numbF")

    val aPb = RAdd(numbA, numbB)
    println("a + b = $aPb")

    val cPdPe = RAdd(RAdd(numbC, numbD), numbE)
    println(cPdPe)
    println(cPdPe.eval())

    val expr = generateCode("TestClass", "double", "func", "double a, double x, double y", "a * x + y")
    println(expr)

    val compiler = CodeCompiler()
    val cls = compiler.compile(expr, "TestClass")
    println(cls.invoke(1, 2, 3))
}

interface RExpression {
    fun eval(): Double
}

class RNumber(private val value: Number): RExpression {
    override fun eval(): Double {
        return value.toDouble()
    }

    override fun toString(): String {
        return value.toString()
    }
}

class RAdd(private val left: RExpression, private val right: RExpression): RExpression {
    override fun eval(): Double {
        return left.eval() + right.eval()
    }

    override fun toString(): String {
        return "$left + $right"
    }
}

fun generateCode(className: String, returnType: String, functionName: String, args: String, expression: String): String {
    return """
        public class {{className}} {
            public {{returnType}} {{functionName}}({{args}}) {
                return {{expression}};
            }
        }
    """
        .trimIndent()
        .replace("{{className}}", className)
        .replace("{{returnType}}", returnType)
        .replace("{{functionName}}", functionName)
        .replace("{{args}}", args)
        .replace("{{expression}}", expression)
}