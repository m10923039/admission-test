def find_max(numbers):
    if len(numbers) > 0:
        temp = numbers[0]
        for values in numbers:
            if values > temp:
                temp = values
        return temp
    return numbers

def find_position(numbers, target):
    target_index = -1
    for i in range(len(numbers)):
        if numbers[i] == target:
            target_index = i
            break
    return target_index


if __name__ == '__main__':
    print(find_max([1, 2, 4, 5]))  # should print 5
    print(find_max([5, 2, 7, 1, 6]))  # should print 7
    print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
    print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
    print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
    print(find_position([5, 2, 7, 1, 6], 8)) # should print -1