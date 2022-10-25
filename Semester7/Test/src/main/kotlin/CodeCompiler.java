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

    public Func compile(String source, String fileName) throws IOException, ClassNotFoundException, InstantiationException, IllegalAccessException, InvocationTargetException, NoSuchMethodException {
        File sourceFile = saveCode(source, fileName);
        compile(sourceFile.getPath());
        return loadClass(sourceFile, fileName);
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

    private Func loadClass(File sourceFile, String className) throws MalformedURLException, ClassNotFoundException, InvocationTargetException, NoSuchMethodException, InstantiationException, IllegalAccessException {
        URLClassLoader classLoader = URLClassLoader.newInstance(new URL[] { sourceFile.getParentFile().toURI().toURL() });
        Class<?> cls = Class.forName(className, true, classLoader);
        return new Func(cls);
    }
}
