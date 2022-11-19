class JavaFunctionPattern(private val className: String, private val function: String, private val args: Map<String, String>, returnType: String, expression: String) {
    val code = """
public class $className {
    public $returnType $function(${argsToList()}) {
        return $expression;
    }
}
"""

    private fun argsToList(): String {
        var result = ""

        args.keys.forEach { variable ->
            val type = args[variable]
            result += if (result == "") {
                "$type $variable"
            } else {
                ", $type $variable"
            }
        }

        return result
    }

    override fun toString(): String {
        return code
    }

    fun getClassName() = className
    fun getFunctionName() = function
}
