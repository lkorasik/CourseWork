package org.example

import kotlin.math.pow

/**
 * Hello world!
 *
 */
fun main(args: Array<String>) {
    val a = 1
//    println(RegimeMap().newRegimeMao(
//            xStart = 0.2,
//            yStart = 0.2,
//            aRange = lst(0.3, 0.5, 0.0001).reversed(),
//            raRange = lst(0.5, 0.5, 0.001),
//            bRange = lst(0.01, 1.0, 0.001),
//            timeRange = 1..10000,
//            f = { b, gg, x, y -> (a * x.pow(2)) / ((b + x).pow(6)) - gg * x * y },
//            g = { b, gg, x, y -> y + gg * y * (x - y) },
//            filePath = "C:\\users\\lkora\\desktop\\ktData\\",
//            accuracy = 5
//    ))

    /*
    println(RegimeMap().newRegimeMap(
        xStart = 0.2,
        yStart = 0.2,
        aRange = lst(0.01, 1.0, 0.001),
        raRange = lst(0.5, 0.5, 0.001),
        bRange = lst(0.3, 0.5, 0.0001).reversed(),
        timeRange = 1..10000,
        f = { gg, b, x, y -> (a * x.pow(2)) / ((b + x).pow(6)) - gg * x * y },
        g = { gg, b, x, y -> y + gg * y * (x - y) },
        filePath = "C:\\users\\lkora\\desktop\\ktData2\\",
        accuracy = 5
    ))
     */

//    println(
//        RegimeMap().newRegimeMap(
//            xStart = 0.2037,
//            yStart = 0.2726,
//            aRange = lst(0.38, 0.405, 0.0001),
//            raRange = lst(0.5, 0.5, 0.001),
//            bRange = lst(0.3, 1.0, 0.001),
//            timeRange = 1..10000,
//            f = { b: Double, gg: Double, x: Double, y: Double -> (a * x.pow(2)) / ((b + x).pow(6)) - gg * x * y },
//            g = { b: Double, gg: Double, x: Double, y: Double -> y + gg * y * (x - y) },
//            filePath = "C:\\users\\lkora\\desktop\\ktData3\\",
//            accuracy = 5
//        )
//    )

    println(
        RegimeMap().newRegimeMap(
            xStart = 0.2,
            yStart = 0.3,
            aRange = lst(0.0, 1.0, 0.001),
            bRange = lst(0.0, 1.0, 0.001),
            timeRange = 1..10000,
            f = { b: Double, ss: Double, x: Double, y: Double -> (a * x.pow(2)) / ((b + x).pow(6)) + ss * (y - x) },
            g = { b: Double, ss: Double, x: Double, y: Double -> (a * y.pow(2)) / ((b + y).pow(6)) - ss * (y - x) },
            filePath = "C:\\users\\lkora\\desktop\\tpy3\\",
            accuracy = 5
        )
    )
}

fun iterator(start: Double, end: Double, step: Double): Iterator<Double> {
    return generateSequence(start) { it + step }
        .takeWhile { it <= end }
        .iterator()
}


fun lst(start: Double, end: Double, step: Double): List<Double> {
    val values = mutableListOf<Double>()
    var current = start
    while (current <= end) {
        values.add(current)
        current += step
    }
    return values
}
