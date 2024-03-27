def multiply_list(lst):
    result = int(lst[0])
    for val in lst[1:]:
        result = result * int(val)
    return result


def main(x):
    x = [digit for digit in x if digit != '0']
    x = str(multiply_list(x))
    if len(x) == 1:
        return x
    return main(x)


if __name__ == '__main__':
    print(main(input()))
