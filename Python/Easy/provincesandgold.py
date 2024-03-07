def main():
    g, s, c = map(int, input().split())
    buying_power = g*3 + s*2 + c
    result_str = ''

    if buying_power >= 8:
        result_str += 'Province'
    elif buying_power >= 5:
        result_str += 'Duchy'
    elif buying_power >= 2:
        result_str += 'Estate'

    if len(result_str) > 0:
        result_str += ' or '

    if buying_power >= 6:
        result_str += 'Gold'
    elif buying_power >= 3:
        result_str += 'Silver'
    else:
        result_str += 'Copper'

    print(result_str)


if __name__ == '__main__':
    main()
