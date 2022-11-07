print ("Lab3 Exercise 2")



def bubble_sort(arr):

    arr_result = arr.copy()
    n = len(arr_result)

    for s in arr_result:
        if type is not int:
            return 3;

    if n == 0:
        return 0;

    if n < 10:
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
                    result = 2

    elif n > 10:
        result = 1

    return result


def main():
    arr = [64, 34, 25, 12, 22, 11, 90, 45, 56, 34, 46]
    result = bubble_sort(arr)
    print(result)



if __name__ == "__main__":
    main()
