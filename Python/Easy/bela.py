def main():
    from sys import stdin
    inp = stdin.readlines()
    suit_b_val = inp[0].split()[1]
    suit_b_val = suit_b_val.strip()

    suit_vals = {
        'A': [11, 11],
        'K': [4, 4],
        'Q': [3, 3],
        'J': [20, 2],
        'T': [10, 10],
        '9': [14, 0],
        '8': [0, 0],
        '7': [0, 0]
    }
    print(sum([suit_vals[entry[0]][entry[1]!=suit_b_val] for entry in inp[1:]]))


if __name__ == '__main__':
    main()
