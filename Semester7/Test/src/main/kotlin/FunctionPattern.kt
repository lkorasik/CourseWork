class FunctionPattern(private val className: String, returnType: String, function: String, args: String, expression: String) {
    val code = """
public class $className {
    public $returnType $function($args) {
        return $expression;
    }
}
"""

    override fun toString(): String {
        return code
    }

    fun getClassName() = className
}
