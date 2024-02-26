def main():
    from sys import stdin
    dir_flights = []
    for i, line in enumerate(stdin.readlines()[1:]):
        for j, val in enumerate(line.split()):
            if val != '-1':
                dir_flights.append(f'{i+1} {j+1} {val}')
    print(len(dir_flights))
    for entry in dir_flights:
        print(entry)


if __name__ == '__main__':
    main()
