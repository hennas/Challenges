from sys import stdin

def main():
    print('\n'.join([f'{int(i)} is {["even", "odd"][int(i)%2]}' for i in stdin.readlines()[1:]]))


if __name__ == '__main__':
    main()
