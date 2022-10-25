package org.example

import java.io.File

class RegimeMap {
    private fun round(value: Double, length: Int): Double {
        var a = 10
        var c = 0
        while (c < length) {
            a *= 10
            c++
        }
        return (value * a).toInt().toDouble() / a
    }

    fun newRegimeMap(
            xStart: Double,
            yStart: Double,
            aRange: List<Double>,
            raRange: List<Double>,
            bRange: List<Double>,
            timeRange: IntRange,
            f: (a: Double, b: Double, x: Double, y: Double) -> Double,
            g: (a: Double, b: Double, x: Double, y: Double) -> Double,
            filePath: String,
            accuracy: Int
    ) {
        val result_x = HashMap<Double, HashMap<Double, MutableList<Double>>>()
        val result_y = HashMap<Double, HashMap<Double, MutableList<Double>>>()
        for (a in aRange) {
            val fk = round(a, accuracy)
            result_x[fk] = HashMap()
            result_y[fk] = HashMap()
            println(fk)
            var x0 = xStart
            var y0 = yStart
            for (b in bRange) {
                val sc = round(b, accuracy)
                result_x[fk]!![sc] = mutableListOf()
                result_y[fk]!![sc] = mutableListOf()
                for (t in timeRange) {
                    val xt = f(a, b, x0, y0)
                    val yt = g(a, b, x0, y0)
                    x0 = xt
                    y0 = yt
                }
                for (t in 1..20) {
                    val xt = f(a, b, x0, y0)
                    val yt = g(a, b, x0, y0)
                    result_x[fk]!![sc]!!.add(xt)
                    result_y[fk]!![sc]!!.add(yt)
                    x0 = xt
                    y0 = yt
                }
            }
        }
        for (a in raRange) {
            val fk = round(a, accuracy)
            result_x[fk] = HashMap()
            result_y[fk] = HashMap()
            println(fk)
            var x0 = xStart
            var y0 = yStart
            for (b in bRange) {
                val sc = round(b, accuracy)
                result_x[fk]!![sc] = mutableListOf()
                result_y[fk]!![sc] = mutableListOf()
                for (t in timeRange) {
                    val xt = f(a, b, x0, y0)
                    val yt = g(a, b, x0, y0)
                    x0 = xt
                    y0 = yt
                }
                for (t in 1..20) {
                    val xt = f(a, b, x0, y0)
                    val yt = g(a, b, x0, y0)
                    result_x[fk]!![sc]!!.add(xt)
                    result_y[fk]!![sc]!!.add(yt)
                    x0 = xt
                    y0 = yt
                }
            }
        }

        println("data collected")

        val res_x = HashMap<Int, MutableList<MutableList<Any>>>()
        val res_y = HashMap<Int, MutableList<MutableList<Any>>>()

        for (j in 1..10) {
            res_x[j] = mutableListOf()
            res_y[j] = mutableListOf()
            for (a in aRange) {
                val fk = round(a, accuracy)
                for (b in bRange) {
                    val sc = round(b, accuracy)
                    val data_x = result_x[fk]!![sc]
                    val data_y = result_y[fk]!![sc]
                    for (i in 0 until data_x!!.size) {
                        data_x[i] = round(data_x[i], accuracy)
                    }
                    for (i in 0 until data_y!!.size) {
                        data_y[i] = round(data_y[i], accuracy)
                    }

                    val di_x = data_x.groupingBy { it }.eachCount()
                    val di_y = data_y.groupingBy { it }.eachCount()
                    if ((di_x.keys.size == j) && (di_y.keys.size == j)) {
                        res_x[j]!!.add(mutableListOf(fk, sc, di_x.keys))
                        res_y[j]!!.add(mutableListOf(fk, sc, di_y.keys))
                        continue
                    }
                }
            }
        }

        /*
        res_x.keys.forEach { key ->
            res_x[key]!!.forEach { item ->
                val fk = item[0] as Double
                val sc = item[1] as Double
                val values = item[2] as Set<*>
                println("$fk $sc $values")
            }
        }
        res_y.keys.forEach { key ->
            res_y[key]!!.forEach { item ->
                val fk = item[0] as Double
                val sc = item[1] as Double
                val values = item[2] as Set<*>
                println("$fk $sc $values")
            }
        }
         */

        val peq_x = File(filePath + "eqX2Gt2X1_x.txt").writer()
        val peq1_x = File(filePath + "eqX2Lt2X1_x.txt").writer()
        val c2_x = File(filePath + "cycle2_x.txt").writer()
        val c3_x = File(filePath + "cycle3_x.txt").writer()
        val c4_x = File(filePath + "cycle4_x.txt").writer()
        val c5_x = File(filePath + "cycle5_x.txt").writer()
        val c6_x = File(filePath + "cycle6_x.txt").writer()
        val c7_x = File(filePath + "cycle7_x.txt").writer()
        val c8_x = File(filePath + "cycle8_x.txt").writer()
        val c9_x = File(filePath + "cycle9_x.txt").writer()
        val c11_x = File(filePath + "cycle11_x.txt").writer()
        val c10_x = File(filePath + "cycle10_x.txt").writer()
        val c12_x = File(filePath + "cycle12_x.txt").writer()
        val c13_x = File(filePath + "cycle13_x.txt").writer()
        val c14_x = File(filePath + "cycle14_x.txt").writer()
        val c15_x = File(filePath + "cycle15_x.txt").writer()

        val peq_y = File(filePath + "eqX2Gt2X1_y.txt").writer()
        val peq1_y = File(filePath + "eqX2Lt2X1_y.txt").writer()
        val c2_y = File(filePath + "cycle2_y.txt").writer()
        val c3_y = File(filePath + "cycle3_y.txt").writer()
        val c4_y = File(filePath + "cycle4_y.txt").writer()
        val c5_y = File(filePath + "cycle5_y.txt").writer()
        val c6_y = File(filePath + "cycle6_y.txt").writer()
        val c7_y = File(filePath + "cycle7_y.txt").writer()
        val c8_y = File(filePath + "cycle8_y.txt").writer()
        val c9_y = File(filePath + "cycle9_y.txt").writer()
        val c11_y = File(filePath + "cycle11_y.txt").writer()
        val c10_y = File(filePath + "cycle10_y.txt").writer()
        val c12_y = File(filePath + "cycle12_y.txt").writer()
        val c13_y = File(filePath + "cycle13_y.txt").writer()
        val c14_y = File(filePath + "cycle14_y.txt").writer()
        val c15_y = File(filePath + "cycle15_y.txt").writer()

        for (j in 1..10) {
            var line = ""
            var k = ""
            for (item in res_x[j]!!) {
                val a = item[0]
                val b = item[1]

                if (j == 1) {
                    if (listOf(item[2]) == listOf(0.0)) {
                        k += "$a $b\n"
                    } else {
                        line += "$a $b\n"
                    }
                } else {
                    line += "$a $b\n"
                }
            }

            if (j == 1) {
                peq1_x.write(k)
                peq_x.write(line)
            }
            if (j == 2)
                c2_x.write(line)
            if (j == 3)
                c3_x.write(line)
            if (j == 4)
                c4_x.write(line)
            if (j == 5)
                c5_x.write(line)
            if (j == 6)
                c6_x.write(line)
            if (j == 7)
                c7_x.write(line)
            if (j == 8)
                c8_x.write(line)
            if (j == 9)
                c9_x.write(line)
            if (j == 10)
                c10_x.write(line)
            if (j == 11)
                c11_x.write(line)
            if (j == 12)
                c12_x.write(line)
            if (j == 13)
                c13_x.write(line)
            if (j == 14)
                c14_x.write(line)
            if (j == 15)
                c15_x.write(line)
        }

        for (j in 1..10) {
            var line = ""
            var k = ""
            for (item in res_y[j]!!) {
                val a = item[0]
                val b = item[1]

                if (j == 1) {
                    if (listOf(item[2]) == listOf(0.0)) {
                        k += "$a $b\n"
                    } else {
                        line += "$a $b\n"
                    }
                } else {
                    line += "$a $b\n"
                }
            }

            if (j == 1) {
                peq1_y.write(k)
                peq_y.write(line)
            }
            if (j == 2)
                c2_y.write(line)
            if (j == 3)
                c3_y.write(line)
            if (j == 4)
                c4_y.write(line)
            if (j == 5)
                c5_y.write(line)
            if (j == 6)
                c6_y.write(line)
            if (j == 7)
                c7_y.write(line)
            if (j == 8)
                c8_y.write(line)
            if (j == 9)
                c9_y.write(line)
            if (j == 10)
                c10_y.write(line)
            if (j == 11)
                c11_y.write(line)
            if (j == 12)
                c12_y.write(line)
            if (j == 13)
                c13_y.write(line)
            if (j == 14)
                c14_y.write(line)
            if (j == 15)
                c15_y.write(line)
        }

        peq1_x.close()
        peq_x.close()
        c2_x.close()
        c3_x.close()
        c4_x.close()
        c5_x.close()
        c6_x.close()
        c7_x.close()
        c8_x.close()
        c9_x.close()
        c10_x.close()
        c11_x.close()
        c12_x.close()
        c13_x.close()
        c14_x.close()
        c15_x.close()

        peq1_y.close()
        peq_y.close()
        c2_y.close()
        c3_y.close()
        c4_y.close()
        c5_y.close()
        c6_y.close()
        c7_y.close()
        c8_y.close()
        c9_y.close()
        c10_y.close()
        c11_y.close()
        c12_y.close()
        c13_y.close()
        c14_y.close()
        c15_y.close()
    }
}