def main():
    input()
    print(max(map(int,''.join([[' ', c][c.isnumeric()] for c in input()]).split())))


if __name__ == '__main__':
    main()
