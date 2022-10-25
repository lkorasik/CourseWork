import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class Func {
    private final Class<?> cls;
    private final Object instance;
    private Method func;

    public Func(Class<?> cls) throws NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {
        this.cls = cls;
        func = cls.getMethod("func", double.class, double.class, double.class);
        instance = cls.getDeclaredConstructors()[0].newInstance();
    }

    public Double invoke(Object... objects) throws InvocationTargetException, IllegalAccessException {
        return (Double) func.invoke(instance, objects);
    }
}
