from sys import stdin, stdout

def print_result(tc, result):
    print(tc, result[-1])
    for i in range(0, len(result), 10):
        stdout.write(' '.join(result[i:i+10]) + '\n')


def main():
    next(stdin)
    for line in stdin:
        tc, num_bins = map(int, line.split())
        result = []
        s = num_bins % 2
        result.append(str(s))
        i = 2
        while s < num_bins:
            stones_in_bin = (num_bins - s) % (i+1)
            s += stones_in_bin
            result.append(str(stones_in_bin))
            i += 1
        print_result(tc, result)


if __name__ == '__main__':
    main()
