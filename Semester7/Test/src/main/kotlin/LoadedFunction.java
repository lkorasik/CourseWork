import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Arrays;

public class LoadedFunction {
    private final Object instance;
    private final Method function;

    public LoadedFunction(Class<?> cls, String functionName) throws InvocationTargetException, InstantiationException, IllegalAccessException {
        function = Arrays.stream(cls.getMethods()).filter(method -> method.getName().equals(functionName)).toList().get(0);
        instance = cls.getDeclaredConstructors()[0].newInstance();
    }

    public Double invoke(Object... objects) throws InvocationTargetException, IllegalAccessException {
        return (Double) function.invoke(instance, objects);
    }
}
