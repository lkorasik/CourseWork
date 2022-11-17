import java.util.*

class FunctionBuilder {
    private var className: String = "a" + UUID.randomUUID().toString().replace("-", "")
    private var returnType: String = "int"
    private var functionName: String = "a" + UUID.randomUUID().toString().replace("-", "")
    private var args: HashMap<String, String> = hashMapOf()
    private var expression: String = "0"

    fun setClassName(className: String): FunctionBuilder {
        this.className = className
        return this
    }

    fun setClassName(getClassName: () -> String): FunctionBuilder {
        className = getClassName()
        return this
    }

    fun setReturnType(returnType: String): FunctionBuilder {
        this.returnType = returnType
        return this
    }

    fun setReturnType(getReturnType: () -> String): FunctionBuilder {
        this.returnType = getReturnType()
        return this
    }

    fun setFunctionName(functionName: String): FunctionBuilder {
        this.functionName = functionName
        return this
    }

    fun setFunctionName(getFunctionName: () -> String): FunctionBuilder {
        this.functionName = getFunctionName()
        return this
    }

    fun addArg(type: String, value: String): FunctionBuilder {
        args[value] = type
        return this
    }

    fun setExpression(expression: String): FunctionBuilder {
        this.expression = expression
        return this
    }

    fun setExpression(getExpression: () -> String): FunctionBuilder {
        expression = getExpression()
        return this
    }

    fun build(): FunctionPattern {
        return FunctionPattern(className, functionName, args, returnType, expression)
    }
}
