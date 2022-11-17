var x = 3
var y = 5

x * y

infix fun Int.pow(v: Int): Int {
    return Math.pow(this.toDouble(), v.toDouble()).toInt()
}

2 pow 3
