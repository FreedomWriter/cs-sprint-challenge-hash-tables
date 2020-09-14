# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    hash_table = {}
    result = []

    

    for file in files:
        paths = file.split('/')
        path= paths[-1]
        # print(path)
        hash_table[path] = file
    print(hash_table)
    for query in queries:
        if query in hash_table:
            result.append(hash_table[query])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
