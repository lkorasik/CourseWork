import javax.tools.JavaCompiler;
import javax.tools.ToolProvider;
import java.io.File;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class CodeCompiler {
    private final Path pathToTempFolder = Path.of(String.valueOf(Paths.get(".").toAbsolutePath()), "temp");

    public LoadedFunction compile(JavaFunctionPattern source)
            throws IOException, ClassNotFoundException, InstantiationException, IllegalAccessException,
            InvocationTargetException {
        File sourceFile = saveCode(source.getCode(), source.getClassName());
        compile(sourceFile.getPath());
        return loadClass(sourceFile, source.getClassName(), source.getFunctionName());
    }

    private File saveCode(String source, String fileName) throws IOException {
        File codeFile = new File(pathToTempFolder.toFile(), fileName + ".java");
        Files.writeString(codeFile.toPath(), source);
        return codeFile;
    }

    private void compile(String path) {
        JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
        compiler.run(null, null, null, path);
    }

    private LoadedFunction loadClass(File sourceFile, String className, String funcName)
            throws MalformedURLException, ClassNotFoundException, InvocationTargetException, InstantiationException,
            IllegalAccessException {
        URLClassLoader classLoader = URLClassLoader.newInstance(new URL[]{
                sourceFile.getParentFile().toURI().toURL()
        });
        Class<?> cls = Class.forName(className, true, classLoader);
        return new LoadedFunction(cls, funcName);
    }
}
