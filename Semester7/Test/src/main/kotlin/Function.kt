class Function(className: String, returnType: String, function: String, args: String, expression: String) {
    val template =
"""
public class $className {
    public $returnType $function($args) {
        return $expression;
    }
}
"""
}
