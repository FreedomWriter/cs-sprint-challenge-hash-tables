def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    result_with_dupes = []
    hash_result = {}
    # result = []
    # print(a)

    for num in a:
        hash_table[num] = True

    for key in hash_table.keys():
        # print(key, key * -1)
        if (key * -1) in hash_table:
            result_with_dupes.append(abs(key))

    for num in result_with_dupes:
        if not num in hash_result:
            hash_result[num] = 0
        hash_result[num] += 1
    
    result = list(hash_result.keys())
    
    # print(hash_result)

    # print(hash_table)

    return result


if __name__ == "__main__":
    # print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
