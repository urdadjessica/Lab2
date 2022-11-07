import bmi
print("Test_Bmi")

def test_bmi_normal_weight():

    height = 1.73
    weight = 57
    test = -1
    result = bmi.calculate_bmi(height, weight)

    assert (result == test)

def test_bmi_over_weight():

    height = 1
    weight = 140
    test = 1

    result = bmi.calculate_bmi(height, weight)

    assert (result == test)

def test_bmi_under_weight():

    height = 40
    weight = 1
    test = 0

    result = bmi.calculate_bmi(height, weight)

    assert (result == test)