import os, sys  # E401: multiple imports on one line


def messy_function(a, b, c=3):  # E231: missing whitespace after ','
    x = a + b * c  # E225: missing whitespace around operator
    if x > 10:  # E225: missing whitespace around comparison
        print("Result is large")  # E202: whitespace before ')'
    return x


def another_function():  # E222: multiple spaces after keyword
    print(
        "This indentation is 5 spaces instead of 4"
    )  # E111: indentation is not a multiple of 4


# E303: too many blank lines (there are 3 blank lines above this)
messy_function(5, 10)  # E201: whitespace after '(' and E202: whitespace before ')'
