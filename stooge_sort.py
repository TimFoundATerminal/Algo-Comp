import math
import numpy as np
import random
# create a function that sorts a list using the stooge sort algorithm


def stooge_sort(x: np.array) -> np.array:
    """Stooge-sort divide and conquer algorithm"""
    n = len(x)

    # Handle the base case when n < 3
    if n < 3:
        if n == 2 and x[0] > x[1]: # taking advantage of python's lazy evaluation
            swap(x, 0, 1)
        return x
    
    one_third = math.floor(n/3) # round to nearest integer
    two_thirds = 2*one_third
    # 1. Sort the top [2n/3]
    x = x[:one_third] + stooge_sort(x[one_third:])
    # 2. Sort the bottom [2n/3]
    x = stooge_sort(x[:two_thirds]) + x[two_thirds:]
    # 3. Sort the top [2n/3] again
    x = x[:one_third] + stooge_sort(x[one_third:])

    return x

# create a swap helper function
def swap(x: np.array, i: int, j: int) -> None:
    """Swap elements i and j in array x"""
    temp = x[i]
    x[i] = x[j]
    x[j] = temp

def main():
    # create a range and shuffle it
    x = list(range(10))
    random.shuffle(x)
    print("Unsorted list: ", x)
    x = stooge_sort(x)
    print("Sorted list: ", x)

if __name__ == "__main__":
    main()

    