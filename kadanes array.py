
def kadanes_algorithm(a):
    n = len(a)
    array_max = sum_max = a[0]
    startI = endI = 0

    for i in range(1, n):
        array_max = max(a[i], a[i] + array_max)

        if array_max > sum_max:
            sum_max = array_max
            endI = i

        if array_max < 0:
            array_max = 0
            startI = i + 1

    print("Subarray máximo:", a[startI:endI + 1])
    print("Suma máxima:", sum_max)

arr = [-2, 1, -3, 4, -1, 2, 1, 8, 2,  -5, 4]
kadanes_algorithm(arr)


