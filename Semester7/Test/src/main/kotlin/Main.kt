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

    val aPb2 = numbA + numbB
    println("a + b = $aPb")

    val cPdPe = RAdd(RAdd(numbC, numbD), numbE)
    println(cPdPe)

    val expr = FunctionBuilder()
        .setClassName { "TestClass" }
        .setReturnType { "double" }
        .setFunctionName { "func" }
        .addArg("double", "a")
        .addArg("double", "x")
        .addArg("double", "y")
        .setExpression { "a * x + y" }
        .build()
    println(expr)

    val compiler = CodeCompiler()
    val cls = compiler.compile(expr)
    println(cls.invoke(1, 2, 3))

    val equation = RAdd(numbC, varX)
    println(equation)
}

interface RExpression

class RNumber(private val value: Number) : RExpression {
    override fun toString(): String {
        return value.toString()
    }

    operator fun plus(other: Byte): RAdd {
        return RAdd(this, RNumber(other))
    }

    operator fun plus(other: Short): RAdd {
        return RAdd(this, RNumber(other))
    }

    operator fun plus(other: Int): RAdd {
        return RAdd(this, RNumber(other))
    }

    operator fun plus(other: Long): RAdd {
        return RAdd(this, RNumber(other))
    }

    operator fun plus(other: Float): RAdd {
        return RAdd(this, RNumber(other))
    }

    operator fun plus(other: Double): RAdd {
        return RAdd(this, RNumber(other))
    }

    operator fun plus(other: RExpression): RAdd {
        return RAdd(this, other)
    }

    operator fun times(other: Byte): RMul {
        return RMul(this, RNumber(other))
    }

    operator fun times(other: Short): RMul {
        return RMul(this, RNumber(other))
    }

    operator fun times(other: Int): RMul {
        return RMul(this, RNumber(other))
    }

    operator fun times(other: Long): RMul {
        return RMul(this, RNumber(other))
    }

    operator fun times(other: Float): RMul {
        return RMul(this, RNumber(other))
    }

    operator fun times(other: Double): RMul {
        return RMul(this, RNumber(other))
    }

    operator fun times(other: RExpression): RMul {
        return RMul(this, other)
    }
}

class RVariable(private val name: String) : RExpression {
    override fun toString(): String {
        return name;
    }
}

class RAdd(private val left: RExpression, private val right: RExpression) : RExpression {
    override fun toString(): String {
        return "$left + $right"
    }
}

class RMul(private val left: RExpression, private val right: RExpression) : RExpression {
    override fun toString(): String {
        return "$left * $right"
    }
}