def swap_case(string):
    swapped = string.swapcase()
    return swapped


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)