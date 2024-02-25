def main():
    from sys import stdin
    inp = stdin.readlines()
    speed = int(inp[0])
    for line in inp[2:]:
        street, max_speed = line.split()
        if speed > int(max_speed):
            print(f'{street} lokud')
        else:
            print(f'{street} opin')

if __name__ == '__main__':
    main()
