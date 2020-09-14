def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # print(f"weights: {weights}")
    # print(f"length: {length}")
    # print(f"limit: {limit}")

    hash_table = {}
    solution = None

    if len(weights) <= 1:
        return None

    if len(weights) == 2:
        if limit - weights[0] - weights[1] == 0:
            return (1, 0)

    for i in range(0, len(weights)):
        if not i in hash_table.values():
            hash_table[weights[i]] = i

    for weight in weights:
        if (limit - weight) in hash_table:
            if hash_table[(limit-weight)] > hash_table[weight]:
                solution = (hash_table[(limit-weight)], hash_table[weight])
            else:
                solution = ( hash_table[weight], hash_table[(limit-weight)])
    return solution


weights_1 = [9]
weights_3 = [4, 6, 10, 15, 16]
weights_2 = [4, 4]
weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# answer_1 = get_indices_of_item_weights(weights_1, 1, 9)
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
# answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
# answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

# print(answer_1)
# print(answer_2)
# print(answer_3)
# print(answer_4)