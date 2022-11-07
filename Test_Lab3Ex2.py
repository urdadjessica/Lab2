import Lab3Ex2

print("Test_Lab3Ex2")


def test_bubble_sort_lessthan10():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test = 2

    result = Lab3Ex2.bubble_sort(input_arr)

    assert (result == test)
    print (result)

def test_bubble_sort_morethan10():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 85, 23, 45, 12]
    test = 1

    result = Lab3Ex2.bubble_sort(input_arr)

    assert (result == test)

def test_bubble_sort_novalue():
    result = []
    input_arr = []
    test = 0

    result = Lab3Ex2.bubble_sort(input_arr)

    assert (result == test)

def test_bubble_sort_whatvalue():
    result = []
    input_arr = [64, 34, 25, 12, 22, "hi", 90, 85, 23, 45]
    test = 3

    result = Lab3Ex2.bubble_sort(input_arr)

    assert (result == test)