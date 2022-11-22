package org.example

import java.nio.file.Path

class Utils {
    companion object {
        fun getProjectPath(): Path = Path.of(".").toAbsolutePath()
    }
}