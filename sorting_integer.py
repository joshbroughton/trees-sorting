#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    max_number = numbers[0]
    min_number = numbers[0]

    # find min_number and max_number, O(n)
    for _, item in enumerate(numbers):
        if item < min_number:
            min_number = item
        if item > max_number:
            max_number = item
    counts_list = [0] * (max_number - min_number + 1)
    print(counts_list)
    print(min_number)
    print(max_number)
    # determine counts, O(n)
    for _, item in enumerate(numbers):
        print(item)
        counts_list[item - min_number] += 1

    i = 0
    j = 0
    while i < len(counts_list):
        while counts_list[i] != 0:
            numbers[j] = i + min_number
            j += 1
            counts_list[i] -= 1
        i +=1



def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
