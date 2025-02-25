import numpy as np
import math


def sort_7(x: np.array) -> np.array:
    """Dummy Sort a list of 7 elements"""
    return np.sort(x)

def greater_than_swap(x_1, x_2) -> tuple:
    """Helper function to swap and rename values"""
    if x_1 < x_2:
        return x_2, x_1
    return x_1, x_2

def sort_5(x: np.array) -> np.array:
    """Sort a list of 5 elements using 7 comparisons"""
    a_1, a_2, b_1, b_2, c = x
    a_1, a_2 = greater_than_swap(a_1, a_2)
    a_1, b_1 = greater_than_swap(a_1, b_1)
    a_2, b_2 = greater_than_swap(a_2, b_2)

    # use a list to approximate a linked list
    chain = [a_1, a_2, b_2]
    i = 0
    while (i < 3 and c < chain[i]):
        i += 1
    chain.insert(i, c)

    # insert b_1 but which we know is greater than a_1
    i = 1
    while (i < 4 and b_1 < chain[i]):
        i += 1
    chain.insert(i, b_1)

    return np.array(chain)



def find_tth(a: np.array, t: int) -> int:
    """Find the t-th largest element in a list"""
    n = len(a)

    # Handle the base case when n < 1024
    if n < 7: # TODO: change to 1024
        a = np.sort(a)
        return a[t]
    
    # Divide the array into chunks of 7 elements
    q = math.ceil((n-7) / 14)
    n_prime = 7*(2*q + 1)

    # Pad the array with np.inf
    a = np.concatenate([a, np.repeat(np.inf, n_prime - n)])

    # # reshape the array into chunks of 7 elements
    # for k in range(1, 2*q+2):
    #     start_index = (k-1)*7
    #     end_index = k*7
    #     a[start_index:end_index] = sort_7(a[start_index:end_index])

    # # get the 7i+3 element of the array
    # s = np.zeros(2*q+1)
    # for i in range(2*q+1):
    #     s[i] = a[7*i+3]

    # s = [s[i] for i in range(2*q+1) if s[i] != np.inf]

    a = a.reshape(-1, 7) # reshape the array into chunks of 7 elements
    a = np.apply_along_axis(sort_7, 1, a) # sort the 7 elements of each chunk
    print(a)
    s = a[:, 3] # get the 4th element of each chunk

    m = find_tth(s, q+1) # (q+1)th element is the median

    return m
    print("m: ", m)


def quicksort(arr: np.array) -> np.array:
    """Quick sort algorithm"""
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (using middle element to avoid worst-case on sorted arrays)
    pivot = arr[len(arr) // 2]
    
    # Partition the array
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort the partitions and combine the results
    return quicksort(left) + middle + quicksort(right)


def main():
    # create a range and shuffle it
    x = np.array(range(1, 31))
    np.random.shuffle(x)
    print("Unsorted list: ", x)
    medium = find_tth(x, 9)
    print("Medium: ", medium)


if __name__ == "__main__":
    main()