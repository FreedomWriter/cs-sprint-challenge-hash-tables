def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    result = []

    for arr in arrays:
        for num in arr:
            if num not in hash_table:
                hash_table[num] = 0
            hash_table[num] += 1

    for key in hash_table.keys():
        if hash_table[key] == len(arrays):
            result.append(key)

    return result
result = intersection([
    [1,2,3],
    [1,4,5],
    [1,6,7]
])

# print(result)

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
