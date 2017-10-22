import random

def random_sort(array):
    def is_sorted(array):
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                return False
        return True
    while not is_sorted(array):
        random.shuffle(array)
    return array

print(random_sort([3, 1, 2, 0]))
