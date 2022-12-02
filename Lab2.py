def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    print("haha")
    display_main_menu()
    string_input = get_input()
    num_list = get_user_input(string_input)
    print(calc_average_temperature(num_list))
    print(calc_min_max_temperature(num_list))
   


def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by ")


def get_input():
    input_num = input()
    return input_num


def get_user_input(string_input):
    list_input = string_input.split(",")
    float_list = [float(number) for number in list_input]
    return float_list


def calc_average_temperature(num_input):
    total = 0
    count = 0
    for number in num_input:
        count += 1
    for number in num_input:
        total = total + number
    average = total / count
    return average


def calc_min_max_temperature(num_input):
    smallestnum = largestnum = num_input[0]

    for i in num_input:
        if i > largestnum:
            largestnum = i

    for i in num_input:
        if i < smallestnum:
            smallestnum = i

    max_min_ = [smallestnum, largestnum]
    return max_min_


if __name__ == "__main__":
    main()




