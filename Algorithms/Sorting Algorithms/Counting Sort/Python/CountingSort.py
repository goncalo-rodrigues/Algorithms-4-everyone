def counting_sort(array, possible_values=range(0,256)):
    counts = [0] * len(possible_values)
    for element in array:
        counts[element] += 1
    current_index = 0
    for i, count in enumerate(counts):
        array[current_index:current_index+count] = [possible_values[i]]*count
        current_index += count
    return array
    
print(counting_sort([5, 1, 30, 3, 30, 1]))
