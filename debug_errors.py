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




data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = [] # This will cause an error
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}") #division by zero error