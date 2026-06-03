import pprint
def filter_and_sort_evens(numbers):
   
    evens = [num for num in numbers if num % 2 == 0]
    return sorted(evens)


def count_character_frequency(text):
  
    frequency = {}
    
    for char in text.lower():
        frequency[char] = frequency.get(char, 0) + 1
        
    return frequency

count_character_frequency("This my task for Basic Data Structures & Algorithms")

if __name__ == "__main__":
   
    print(f"Input List:  [3, 1, 4, 7, 1, 5, 9, 2, 6, 8]")
    print(f"Result:      {filter_and_sort_evens([3, 1, 4, 7, 1, 5, 9, 2, 6, 8])}")
    print()

    print("Resulting Dictionaryfor: This my task for Basic Data Structures & Algorithms")
    pprint.pprint(count_character_frequency("This my task for Basic Data Structures & Algorithms"))