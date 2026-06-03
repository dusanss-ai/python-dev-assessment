def calculate_average(numbers):
    total = 0
    lengt = len(numbers)
    try:
        for i in range(len(numbers)):
            total += numbers[i]
    # Logical Error: Incorrect average calculation for empty list
        result = total / len(numbers)
        return result

    except ZeroDivisionError:  
        print("Division with zero is not possible, your list is empty, add numbers")
        return None  # Return a default value so the program doesn't crash
    except TypeError:
        print("Error: The list contains non-numeric elements.")
        return None    
    except Exception:  
        print("There is an error in code that is not covered with error handling")
        return None
""" 
Add another function get_list_element(my_list, index) that attempts to return an element at a given index.
Implement try-except to catch IndexError if the index is out of bounds and TypeError if my_list is not a list.
Print a user-friendly error message for each case and return None.
Include your own example calls to get_list_element with valid, out-of-bounds, and incorrect type inputs. """

def get_list_element(my_list, index):
    try:
        element = my_list[index]
        return element

    except IndexError:
        print("index is out of bounds,you are trying to read system memory :) , return to your list")
        return None
    except TypeError:
        print("my_list is not a list")
        return None
    except Exception:  
        print("There is an error in code that is not covered with error handling")
        return None

"""
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = [] # This will cause an error
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}") #division by zero error"""

data1_example2 = [10, 20, 30, 40, 50]
data2_example2 = 6
data3_example2 = [] # This will cause an error
print(f"Elemtent is: {get_list_element(data1_example2,3)}")
print(f"Elemtent is: {get_list_element(data2_example2,1)}") #Not a list
print(f"Elemtent is: {get_list_element(data3_example2,5)}") #outside scope of list