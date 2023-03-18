def count(input):
    vaules_count = {}
    for values in input:
        temp = vaules_count.get(values)
        if temp is None:
            vaules_count.update({values:1})
        else:
            vaules_count.update({values: temp+1})
    return vaules_count


def group_by_key(input):
    vaules_count = {}
    for values in input:
        key = values.get('key')
        value = values.get('value')
        temp = vaules_count.get(key)
        if temp is None:
            vaules_count.update({key: value})
        else:
            vaules_count.update({key: temp + value})
    return vaules_count


if __name__ == '__main__':
    # your code here
    # input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
    input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x',
              'b', 'c', 'a', 'c', 'a', 'x',
              'b', 'c', 'a', 'c', 'a', 'x',
              'b', 'c', 'a', 'c', 'a', 'x'
              ]

    print(count(input1))  # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}
    #
    # # your code here
    input2 = [
        {'key': 'w', 'value': 3},
        {'key': 'a', 'value': 3},
        {'key': 'b', 'value': 1},
        {'key': 'c', 'value': 2},
        {'key': 'a', 'value': 3},
        {'key': 'c', 'value': 5}
    ]
    print(group_by_key(input2))  # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
