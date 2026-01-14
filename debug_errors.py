def calculate_average(numbers):
    try:
        total = sum(numbers)
        return total / len(numbers)
    except ZeroDivisionError:
        return 0  # return 0 if list is empty


def get_list_element(my_list, index):
    if not isinstance(my_list, list):
        print("Error: Input is not a valid list.")
        return None
    try:
        return my_list[index]
    except IndexError:
        print("Error: Index is out of range.")
        return None



data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []


print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")


print(get_list_element(data1, 2))        
print(get_list_element(data1, 10))       
print(get_list_element("not a list", 0)) 
